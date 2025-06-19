# Module Odoo Chatbot MCP - Intelligence Artificielle

Un module Odoo 18.0 avancé intégrant l'intelligence artificielle Claude d'Anthropic via le protocole MCP (Model Context Protocol) avec Gradio.

## Fonctionnalités

- ✅ **Chatbot IA intégré** avec Claude 3.5 Sonnet d'Anthropic
- ✅ **Protocole MCP** pour l'accès aux données Odoo en temps réel
- ✅ **Interface Gradio** pour serveur MCP externe
- ✅ **Service centralisé** pour appels API optimisés
- ✅ **Configuration flexible** avec multiple modèles Claude
- ✅ **Tests intégrés** pour validation de connexion
- ✅ **Architecture modulaire** respectant les bonnes pratiques Odoo
- ✅ **Compatible Docker** pour déploiement facile

## Architecture

### Composants Principaux

1. **Service Anthropic** (`anthropic_service.py`) - Service centralisé pour appels API
2. **Configuration Chatbot** (`chatbot_config.py`) - Gestion des paramètres
3. **Wizard Chatbot** (`chatbot_wizard.py`) - Interface utilisateur
4. **Contrôleur API** (`chatbot_controller.py`) - Endpoints REST
5. **Messages** (`chatbot_message.py`) - Historique des conversations

### Modèles Claude Supportés

- **Claude 3.5 Sonnet** (Recommandé) - Équilibre performance/coût
- **Claude 3.5 Haiku** - Rapide et économique
- **Claude 3 Opus** - Maximum de puissance
- **Claude 3 Sonnet** - Version antérieure
- **Claude 3 Haiku** - Version antérieure

## Prérequis

### Technique
- Docker & Docker Compose
- Odoo 18.0
- Python 3.8+
- PostgreSQL

### API & Services
- **Clé API Anthropic** : [console.anthropic.com](https://console.anthropic.com/)
- **Serveur MCP Gradio** : Serveur externe pour accès aux données

## Installation

### 1. Cloner le Repository
```bash
git clone https://github.com/votre-repo/odoo-chatbot-mcp.git
cd odoo-chatbot-mcp
```

### 2. Configuration Docker
```bash
# Démarrer les conteneurs
docker-compose up -d

# Vérifier le statut
docker-compose ps
```

### 3. Accès Odoo
- **URL** : http://localhost:8069
- **Utilisateur** : `admin`
- **Mot de passe** : `admin`

### 4. Exposition du Serveur Local (Optionnel)

Pour rendre votre instance Odoo accessible depuis l'extérieur (utile pour les tests avec des services externes ou le partage), utilisez **cloudflared tunnel** :

```bash
# Installer cloudflared (si pas déjà fait)
# macOS
brew install cloudflared

# Linux
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared.deb

# Créer un tunnel vers votre instance locale
cloudflared tunnel --url http://localhost:8069
```

Le tunnel génèrera une URL publique temporaire (ex: `https://xxxx-xx-xx-xx-xx.trycloudflare.com`) que vous pourrez utiliser pour accéder à votre instance Odoo depuis n'importe où.

**⚠️ Important :** Cette URL est temporaire et change à chaque redémarrage du tunnel. Utilisez cette méthode uniquement pour les tests et développement.

### 5. Installation du Module
1. Aller dans **Apps**
2. Rechercher "Chatbot MCP"
3. Cliquer **Install**

## ⚙️ Configuration

### 1. Configuration Initiale

Aller dans **Chatbot MCP > Configuration** :

```
Nom : Configuration Production
Clé API Anthropic : sk-ant-api03-...
Modèle Claude : Claude 3.5 Sonnet (Recommandé)
URL MCP : http://localhost:8080
Actif : ✓
```

### 2. Tests de Connexion

- **Test MCP Complet** : Teste la chaîne complète (Odoo → MCP → Anthropic)
- **Test API Anthropic** : Teste uniquement l'API Anthropic

### 3. Serveur MCP Gradio

Votre serveur MCP doit exposer une API compatible à l'URL configurée.

## Utilisation

### Interface Principale

1. **Menu** → **Chatbot MCP** → **Ouvrir Chatbot**
2. Saisir votre question dans le champ texte
3. Cliquer **Envoyer**
4. Recevoir la réponse formatée de Claude

### Exemples de Questions

```
"Montre-moi les statistiques CRM de ce mois"
"Analyse les leads avec le plus fort potentiel"
"Quelles sont les dernières commandes importantes ?"
"Surveille les performances de vente cette semaine"
"Liste les clients les plus actifs"
```

### API REST

Le module expose également des endpoints REST :

```bash
# Envoyer un message
POST /api/chatbot/send_message
{
    "user_input": "Votre question"
}

# Récupérer l'historique
GET /api/chatbot/get_messages?limit=10
```

## 📁 Structure du Projet

```
odoo-chatbot-mcp/
├── docker-compose.yml                 # Configuration Docker
├── odoo.conf                         # Configuration Odoo
├── mon_module_simple/                # Module principal
│   ├── __init__.py
│   ├── __manifest__.py              # Manifest du module
│   ├── models/                      # Modèles de données
│   │   ├── __init__.py
│   │   ├── anthropic_service.py     # Service API centralisé
│   │   ├── chatbot_config.py        # Configuration
│   │   ├── chatbot_wizard.py        # Interface utilisateur
│   │   └── chatbot_message.py       # Historique
│   ├── controllers/                 # Contrôleurs web
│   │   └── chatbot_controller.py    # API REST
│   ├── views/                       # Vues XML
│   │   ├── chatbot_v18.xml         # Vues configuration
│   │   ├── chatbot_wizard_view.xml  # Vue chatbot
│   │   └── chatbot_messages.xml     # Vue messages
│   ├── security/                    # Droits d'accès
│   │   └── ir.model.access.csv
│   └── static/                      # Ressources statiques
│       └── src/scss/
└── README.md
```

## 🔧 Développement

### Architecture du Service

Le module utilise un **service centralisé** (`anthropic_service.py`) qui :

- ✅ Évite la duplication de code
- ✅ Centralise la logique d'appel API
- ✅ Gère les erreurs de manière cohérente
- ✅ Optimise les performances
- ✅ Facilite la maintenance

### Méthodes Principales

```python
# Service Anthropic
anthropic_service = self.env['anthropic.service']

# Appel avec MCP
response = anthropic_service.call_anthropic_api(message, config)

# Appel direct
response = anthropic_service.call_anthropic_direct(message, config)

# Post-traitement
formatted = anthropic_service.post_process_with_llm(response, query, config)
```

### Commandes de Développement

```bash
# Redémarrer Odoo
docker-compose restart odoo

# Logs en temps réel
docker-compose logs -f odoo

# Mise à jour du module
# Via interface Odoo : Apps > Chatbot MCP > Upgrade

# Reset complet
docker-compose down -v && docker-compose up -d
```

## Tests & Validation

### Tests Automatisés

Le module inclut des tests de validation :

```python
# Test de connexion MCP
config.test_connection()

# Test API Anthropic direct
config.test_anthropic_direct()
```

### Validation des Données

- ✅ Format de la clé API Anthropic
- ✅ URL MCP accessible
- ✅ Configuration unique active
- ✅ Gestion d'erreurs robuste

## Dépannage

### Problèmes Courants

**1. Erreur "Invalid fields"**
```bash
# Vérifier les logs
docker-compose logs odoo | grep -i error

# Redémarrer le module
# Apps > Chatbot MCP > Upgrade
```

**2. Clé API invalide**
- Vérifier le format : `sk-ant-api03-...`
- Tester sur console.anthropic.com

**3. Serveur MCP inaccessible**
- Vérifier l'URL et le port
- Tester la connectivité réseau

**4. Réponses "KO"**
- Vérifier les logs du service
- Tester les connexions individuellement

### Logs Utiles

```bash
# Logs du service Anthropic
docker-compose logs odoo | grep "anthropic_service"

# Logs du chatbot
docker-compose logs odoo | grep "chatbot"

# Erreurs générales
docker-compose logs odoo | grep -i "error\|traceback"
```

## 🔒 Sécurité

- ✅ **Clés API** stockées avec `password=True`
- ✅ **Droits d'accès** granulaires par modèle
- ✅ **Validation** des entrées utilisateur
- ✅ **Gestion d'erreurs** sans exposition de données sensibles

## Contribution

1. **Fork** le projet
2. **Créer** une branche feature (`git checkout -b feature/AmazingFeature`)
3. **Committer** vos changements (`git commit -m 'Add AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrir** une Pull Request

### Standards de Code

- Suivre les [conventions Odoo 18.0](https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html)
- Tests unitaires pour nouvelles fonctionnalités
- Documentation des méthodes publiques
- Respect PEP 8 pour Python

## 📄 Licence

Ce projet est sous licence **LGPL-3**. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Lucas Bometon** - [GitHub](https://github.com/lucasbometon)

## 🙏 Remerciements

- [Anthropic](https://www.anthropic.com/) pour l'API Claude
- [Odoo SA](https://www.odoo.com/) pour le framework
- [Gradio](https://gradio.app/) pour l'interface MCP
- Communauté Odoo pour le support

## 📚 Ressources

- [Documentation Odoo 18.0](https://www.odoo.com/documentation/18.0/)
- [API Anthropic](https://docs.anthropic.com/)
- [Protocol MCP](https://github.com/modelcontextprotocol)
- [Docker Documentation](https://docs.docker.com/)

---

**Version** : 1.0.0  
**Compatibilité** : Odoo 18.0  
**Dernière mise à jour** : Décembre 2024 