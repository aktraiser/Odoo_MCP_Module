# 🤖 Chatbot MCP Odoo - Version Moderne

## 📋 Présentation

Module Odoo moderne pour chatbot avec intégration MCP Gradio et API Anthropic Claude, incluant une interface de chat moderne, un historique des conversations et des fonctionnalités interactives avancées.

## ✨ Nouvelles Fonctionnalités (v1.1.0)

### 🎨 Interface Chat Moderne
- **Bulles de messages** avec design moderne type messagerie
- **Interface responsive** s'adaptant à tous les écrans
- **Animations fluides** pour une meilleure expérience utilisateur
- **Mode sombre** automatique selon les préférences système

### 📚 Historique des Conversations
- **Sauvegarde automatique** de tous les échanges
- **Recherche avancée** dans l'historique
- **Sessions utilisateur** pour organiser les conversations
- **Statistiques d'usage** et temps de réponse

### ⚡ Interactivité JavaScript
- **Auto-scroll** des messages
- **Indicateur de frappe** en temps réel
- **Envoi par Entrée** (Shift+Entrée pour nouvelle ligne)
- **Chargement asynchrone** de l'historique

### 🔧 Améliorations Techniques
- **Traçabilité complète** des messages
- **Gestion d'erreurs** robuste
- **Performance optimisée** avec lazy loading
- **Métadonnées enrichies** (temps de réponse, utilisateur, session)

## 🗂 Structure du Module

```
MCP_Odoo/
├── 📁 models/
│   ├── chatbot_message.py      # ✨ Modèle enrichi avec historique
│   ├── chatbot_wizard.py       # ✨ Interface moderne améliorée
│   ├── chatbot_config.py       # Configuration MCP
│   └── anthropic_service.py    # Service API Anthropic
├── 📁 views/
│   ├── chatbot_wizard_view.xml # ✨ Interface chat moderne
│   ├── chatbot_messages.xml    # ✨ Vues historique enrichies
│   └── chatbot_v18.xml         # Menu et configuration
├── 📁 static/src/
│   ├── 📁 scss/
│   │   └── chatbot_modal.scss  # ✨ Styles modernes
│   ├── 📁 js/
│   │   └── chatbot_widget.js   # ✨ Widget JavaScript OWL
│   └── 📁 xml/
│       └── chatbot_templates.xml # ✨ Templates QWeb
└── 📁 security/
    └── ir.model.access.csv     # Permissions d'accès
```

## 🚀 Installation et Configuration

### 1. Installation du Module
```bash
# Copier le module dans addons
cp -r MCP_Odoo /path/to/odoo/addons/

# Mettre à jour la liste des modules
./odoo-bin -u MCP_Odoo -d your_database
```

### 2. Configuration MCP
1. Aller dans **Paramètres > Chatbot MCP > Configuration**
2. Configurer votre **clé API Anthropic**
3. Définir l'**URL de votre serveur MCP Gradio**
4. Activer la configuration

### 3. Utilisation
- Menu : **Chatbot > Assistant MCP**
- Ou : **⚙️ Recherche globale > "Assistant Chatbot"**

## 💬 Utilisation de l'Interface Chat

### Fonctionnalités Principales
- **Envoi de messages** : Tapez votre question et appuyez sur Entrée
- **Historique** : Cliquez sur 📋 pour voir vos conversations passées
- **Effacer** : 🗑️ pour réinitialiser la conversation courante
- **Configuration** : ⚙️ pour ajuster les paramètres

### Exemples de Commandes
```
"Liste les leads"
"Statistiques CRM de ce mois"
"Recherche commandes en attente"
"Analyser les devis récents"
"Créer un nouveau lead pour l'entreprise ABC"
```

## 📊 Fonctionnalités d'Historique

### Vue Liste
- **Filtres avancés** par statut, date, utilisateur
- **Recherche textuelle** dans questions et réponses
- **Codes couleur** selon le statut (✅ traité, ❌ erreur, ⏳ en cours)

### Vue Détail
- **Conversation complète** avec timing
- **Métadonnées** de performance
- **Actions** : rejouer, analyser
- **Statistiques** de session

### Statistiques
- **Temps de réponse moyen**
- **Taux de succès**
- **Utilisation par utilisateur**
- **Graphiques d'évolution**

## 🎨 Personnalisation CSS

### Variables de Couleurs
```scss
$primary-color: #875A7B;  // Violet Odoo
$success-color: #27AE60;  // Vert succès
$text-dark: #2C3E50;      // Texte principal
$text-light: #7F8C8D;     // Texte secondaire
```

### Classes Principales
- `.chatbot-container` : Container principal
- `.chat-conversation` : Zone de messages
- `.chat-message` : Bulle de message
- `.chat-input-area` : Zone de saisie
- `.chat-actions` : Boutons d'action

## 🔧 API et Développement

### Méthodes du Modèle Message
```python
# Historique utilisateur
messages = self.env['chatbot_custom.message'].get_conversation_history(limit=10)

# Statistiques
stats = self.env['chatbot_custom.message'].get_statistics()

# Sessions utilisateur
sessions = self.env['chatbot_custom.message'].get_user_sessions()
```

### Événements JavaScript
```javascript
// Envoyer un message
await this.sendMessage()

// Charger l'historique
await this.loadConversationHistory()

// Rejouer une conversation
await this.loadHistoryConversation(messageId)
```

## 🛠 Dépannage

### Problèmes Courants

#### Interface ne s'affiche pas
- Vérifiez que les assets sont compilés : `./odoo-bin --dev=all`
- Videz le cache navigateur : Ctrl+F5

#### Messages non sauvegardés
- Vérifiez les permissions dans `ir.model.access.csv`
- Contrôlez les logs Odoo pour les erreurs

#### Styles CSS non appliqués
- Vérifiez que le fichier SCSS est dans `web.assets_backend`
- Compilez les assets : Menu Développeur > Régénérer les Assets

#### JavaScript non fonctionnel
- Vérifiez la console navigateur pour les erreurs
- Assurez-vous que OWL est disponible (Odoo 15+)

## 📝 Changelog

### Version 1.1.0 (Actuelle)
- ✨ Interface chat moderne avec bulles
- ✨ Historique complet des conversations
- ✨ Widget JavaScript interactif
- ✨ Styles CSS modernes et responsifs
- ✨ Traçabilité et statistiques avancées
- ✨ Gestion d'erreurs améliorée
- ✨ Templates QWeb pour composants

### Version 1.0.0 (Précédente)
- 🔧 Interface basique avec textarea
- 🔧 Intégration MCP Gradio
- 🔧 Service Anthropic Claude
- 🔧 Configuration de base

## 🤝 Contribution

Pour contribuer à ce projet :
1. Forkez le repository
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements
4. Soumettez une Pull Request

## 📄 Licence

Ce module est sous licence LGPL-3. Voir le fichier LICENSE pour plus de détails.

## 🔗 Liens Utiles

- [Documentation Odoo](https://www.odoo.com/documentation)
- [Framework OWL](https://github.com/odoo/owl)
- [API Anthropic](https://docs.anthropic.com/)
- [MCP Gradio](https://gradio.app/)

---

💡 **Astuce** : Utilisez les raccourcis clavier pour une navigation plus rapide dans l'interface ! 