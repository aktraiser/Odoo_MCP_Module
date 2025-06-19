from odoo import models, api
import requests
import json
import logging

_logger = logging.getLogger(__name__)

class AnthropicService(models.AbstractModel):
    """Service commun pour les appels API Anthropic avec ou sans MCP"""
    _name = 'anthropic.service'
    _description = 'Service Anthropic centralisé'
    
    # Constantes
    ANTHROPIC_API_URL = 'https://api.anthropic.com/v1/messages'
    DEFAULT_MODEL = 'claude-3-5-sonnet-20241022'
    DEFAULT_MAX_TOKENS = 1000
    MCP_TIMEOUT = 30
    DIRECT_TIMEOUT = 15
    
    @api.model
    def call_anthropic_api(self, user_input, config):
        """Point d'entrée principal pour appeler l'API Anthropic"""
        try:
            # Si une URL MCP est configurée, utiliser le MCP Connector
            if config and getattr(config, 'mcp_url', None) and config.anthropic_api_key:
                _logger.info("Utilisation du mode MCP Connector")
                return self.call_anthropic_with_mcp(user_input, config)
            # Sinon, utiliser Anthropic direct
            elif config and config.anthropic_api_key:
                _logger.info("Utilisation du mode Anthropic direct")
                return self.call_anthropic_direct(user_input, config)
            else:
                return "KO : Clé API Anthropic requise pour utiliser le chatbot."
        except Exception as e:
            _logger.error(f"Erreur dans call_anthropic_api: {str(e)}")
            return f"KO : Erreur lors de l'appel API: {str(e)}"
    
    @api.model
    def call_anthropic_with_mcp(self, user_input, config, max_tokens=None, custom_prompt=None):
        """Utilise l'API Anthropic MCP Connector pour se connecter au serveur MCP"""
        try:
            # Préparer l'URL MCP selon la documentation Anthropic
            mcp_url = self._prepare_mcp_url(config.mcp_url)
            
            # Utiliser un prompt personnalisé ou le prompt par défaut
            content = custom_prompt or self._build_mcp_prompt(user_input)
            
            # Payload selon la documentation Anthropic MCP Connector
            anthropic_payload = {
                'model': config.anthropic_model or self.DEFAULT_MODEL,
                'max_tokens': max_tokens or self.DEFAULT_MAX_TOKENS,
                'messages': [
                    {
                        'role': 'user',
                        'content': content
                    }
                ],
                'mcp_servers': [
                    {
                        'type': 'url',
                        'url': mcp_url,
                        'name': 'odoo-mcp-server',
                        'tool_configuration': {
                            'enabled': True
                        }
                    }
                ]
            }
            
            # Headers selon la documentation Anthropic
            headers = {
                'Content-Type': 'application/json',
                'x-api-key': config.anthropic_api_key,
                'anthropic-version': '2023-06-01',
                'anthropic-beta': 'mcp-client-2025-04-04'  # Header beta requis
            }
            
            _logger.info(f"Appel API Anthropic MCP vers: {mcp_url}")
            
            # Appel à l'API Anthropic
            response = requests.post(
                self.ANTHROPIC_API_URL,
                json=anthropic_payload,
                headers=headers,
                timeout=self.MCP_TIMEOUT
            )
            
            return self._process_anthropic_response(response, mcp_url)
                
        except Exception as e:
            _logger.error(f"Erreur Anthropic MCP Connector: {str(e)}")
            return f"""KO : **Erreur Anthropic MCP Connector**

**Erreur :** {str(e)}

**Cette méthode utilise l'API Anthropic officielle pour se connecter aux serveurs MCP.**
**Documentation :** https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector"""
    
    @api.model
    def call_anthropic_direct(self, user_input, config, max_tokens=None):
        """Appel direct vers l'API Anthropic sans MCP"""
        try:
            anthropic_payload = {
                'model': config.anthropic_model or self.DEFAULT_MODEL,
                'max_tokens': max_tokens or self.DEFAULT_MAX_TOKENS,
                'messages': [
                    {
                        'role': 'user',
                        'content': user_input
                    }
                ]
            }
            
            response = requests.post(
                self.ANTHROPIC_API_URL,
                json=anthropic_payload,
                headers={
                    'Content-Type': 'application/json',
                    'x-api-key': config.anthropic_api_key,
                    'anthropic-version': '2023-06-01'
                },
                timeout=self.DIRECT_TIMEOUT
            )
            
            if response.status_code == 200:
                data = response.json()
                if 'content' in data and len(data['content']) > 0:
                    return f"{data['content'][0].get('text', 'Réponse Anthropic')}"
                else:
                    return "Réponse reçue d'Anthropic"
            else:
                _logger.error(f"Erreur API Anthropic: {response.status_code} - {response.text[:100]}")
                return f"KO : Erreur Anthropic {response.status_code}: {response.text[:100]}"
                
        except Exception as e:
            _logger.error(f"Erreur lors de l'appel direct Anthropic: {str(e)}")
            return f"KO : Erreur API Anthropic: {str(e)}"
    
    @api.model
    def post_process_with_llm(self, raw_response, original_query, config):
        """Post-traite la réponse MCP avec le LLM pour la rendre plus lisible"""
        try:
            # Extraire les données importantes de la réponse brute
            data_section = raw_response
            
            # Si on trouve des données JSON brutes, les extraire
            if "[{'role': 'assistant'" in raw_response:
                start_json = raw_response.find("[{'role': 'assistant'")
                if start_json != -1:
                    data_section = raw_response[start_json:]
            elif "**Résultats :**" in raw_response:
                data_section = raw_response.split("**Résultats :**")[1]
                if "**Réponse de l'assistant :**" in data_section:
                    data_section = data_section.split("**Réponse de l'assistant :**")[0]
            
            # Limiter la taille des données pour éviter les erreurs de token
            if len(data_section) > 3000:
                data_section = data_section[:3000] + "... (données tronquées)"
            
            # Prompt pour reformater
            reformat_prompt = f"""Tu es un expert en présentation de données Odoo CRM/Sales.

Question originale de l'utilisateur : "{original_query}"

Données brutes récupérées du système MCP Odoo :
{data_section}

Instructions importantes :
1. Ces données proviennent d'un système MCP Odoo et peuvent contenir du JSON brut
2. Reformate ces données de manière claire et professionnelle
3. Crée des sections bien organisées avec des titres (utilisez des # pour les titres)
4. Utilise des listes à puces pour les éléments
5. Ajoute des emojis pertinents pour rendre la lecture agréable
6. Résume les points clés en début de réponse
7. Mets en évidence les informations importantes (montants, nombres, statuts)
8. Si ce sont des leads, organise par priorité ou montant
9. Réponds en français et sois précis
10. Ignore les métadonnées techniques comme 'role', 'metadata', etc.

Présente ces données de façon claire et attrayante pour un utilisateur d'Odoo."""
            
            formatted_response = self.call_anthropic_direct(reformat_prompt, config, max_tokens=1200)
            
            if formatted_response and len(formatted_response) > 50 and not formatted_response.startswith("KO"):
                return f"OK : **Connexion MCP réussie !**\n\n{formatted_response}"
            
            return None  # Retourner None si le reformatage échoue
                
        except Exception as e:
            _logger.error(f"Erreur lors du post-processing: {str(e)}")
            return None
    
    def _prepare_mcp_url(self, mcp_url):
        """Prépare l'URL MCP selon les standards requis"""
        # S'assurer que l'URL se termine par /sse pour SSE transport
        if not mcp_url.endswith('/sse') and '/gradio_api/mcp/sse' not in mcp_url:
            if mcp_url.endswith('/gradio_api/mcp'):
                mcp_url = mcp_url + '/sse'
            elif '/gradio_api/mcp' not in mcp_url:
                mcp_url = mcp_url.rstrip('/') + '/gradio_api/mcp/sse'
        return mcp_url

    def _build_mcp_prompt(self, user_input):
        """Construit le prompt optimisé pour MCP"""
        return f"""Tu es un assistant Odoo CRM & Sales connecté à un serveur MCP.

Requête utilisateur : "{user_input}"

Instructions :
1. Utilise les outils MCP disponibles pour répondre à la requête
2. Si la requête concerne les leads, utilise les outils d'analyse des leads
3. Si elle concerne les statistiques, utilise les outils de stats CRM/Sales
4. Si elle concerne le monitoring, utilise les outils de surveillance
5. Réponds en français et sois précis

Traite cette requête avec les outils MCP appropriés."""

    def _process_anthropic_response(self, response, mcp_url):
        """Traite la réponse de l'API Anthropic"""
        if response.status_code == 200:
            data = response.json()
            
            # Extraire la réponse selon la documentation
            if 'content' in data and len(data['content']) > 0:
                return self._format_mcp_response(data['content'])
            else:
                return "Réponse reçue d'Anthropic MCP"
        
        elif response.status_code == 400:
            error_data = response.json() if response.headers.get('content-type', '').startswith('application/json') else {}
            error_message = error_data.get('error', {}).get('message', response.text[:200])
            
            return f"""KO : **Erreur de configuration MCP**

**Détails :** {error_message}

**Solutions possibles :**
1. **URL MCP incorrecte :** Vérifiez que l'URL se termine par `/sse`
2. **Serveur MCP inaccessible :** Le serveur {mcp_url} n'est peut-être pas public
3. **Format d'URL :** Essayez `{mcp_url.replace('/sse', '').rstrip('/')}/gradio_api/mcp/sse`

**URL testée :** {mcp_url}"""
        
        else:
            return f"""KO : **Erreur API Anthropic**

**Statut :** {response.status_code}
**Erreur :** {response.text[:200]}

**Vérifiez :**
1. Clé API Anthropic valide
2. Quota API disponible
3. URL MCP accessible : {mcp_url}"""

    def _format_mcp_response(self, content_blocks):
        """Formate la réponse MCP de manière optimisée"""
        # Construire la réponse en analysant tous les blocs de contenu
        main_response = []
        mcp_tools_used = []
        tool_results = []
        
        for block in content_blocks:
            if block.get('type') == 'text':
                text_content = block.get('text', '').strip()
                if text_content:
                    main_response.append(text_content)
            elif block.get('type') == 'mcp_tool_use':
                tool_name = block.get('name', 'Outil inconnu')
                server_name = block.get('server_name', 'serveur inconnu')
                mcp_tools_used.append(f"🔧 **{tool_name}** (serveur: {server_name})")
            elif block.get('type') == 'mcp_tool_result':
                if not block.get('is_error', False):
                    tool_content = block.get('content', [])
                    if tool_content and len(tool_content) > 0:
                        result_text = tool_content[0].get('text', str(tool_content))
                        # Nettoyer et formater le résultat
                        if result_text and result_text.strip():
                            tool_results.append(result_text.strip())
        
        # Construire la réponse finale avec un meilleur formatage
        final_parts = []
        
        # En-tête de succès
        if mcp_tools_used:
            final_parts.append("OK : **Connexion MCP réussie !**")
            final_parts.append("")
            
            # Outils utilisés
            final_parts.append("**Outils utilisés :**")
            for tool in mcp_tools_used:
                final_parts.append(f"   • {tool}")
            final_parts.append("")
        
        # Résultats des outils
        if tool_results:
            final_parts.append("**Résultats :**")
            final_parts.append("")
            
            for i, result in enumerate(tool_results, 1):
                if len(tool_results) > 1:
                    final_parts.append(f"**Résultat {i} :**")
                
                # Traiter les résultats complexes (JSON ou texte formaté)
                if result.startswith('[{') or result.startswith('{'):
                    try:
                        # Tenter de parser le JSON pour un meilleur affichage
                        parsed = json.loads(result)
                        if isinstance(parsed, list) and len(parsed) > 0:
                            first_item = parsed[0]
                            if isinstance(first_item, dict) and 'content' in first_item:
                                content = first_item['content']
                                # Formater le contenu avec des sauts de ligne appropriés
                                formatted_content = content.replace('\\n', '\n')
                                final_parts.append(formatted_content)
                            else:
                                final_parts.append(str(parsed))
                        else:
                            final_parts.append(str(parsed))
                    except json.JSONDecodeError:
                        # Si le parsing JSON échoue, afficher tel quel
                        final_parts.append(result)
                else:
                    # Texte simple - améliorer le formatage
                    formatted_result = result.replace('\\n', '\n')
                    final_parts.append(formatted_result)
                
                if i < len(tool_results):
                    final_parts.append("")  # Séparer les résultats multiples
        
        # Réponse principale de l'assistant
        if main_response:
            if tool_results:  # Si on a des résultats, séparer
                final_parts.append("")
                final_parts.append("**Réponse de l'assistant :**")
                final_parts.append("")
            
            for response_part in main_response:
                # Améliorer le formatage du texte principal
                formatted_response = response_part.replace('\\n', '\n')
                final_parts.append(formatted_response)
        
        # Joindre avec des sauts de ligne
        return "\n".join(final_parts) 