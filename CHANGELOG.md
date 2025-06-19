# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-19

### 🎉 Première version

#### Ajouté
- **Chatbot IA intégré** avec Claude 3.5 Sonnet d'Anthropic
- **Service centralisé** (`anthropic_service.py`) pour appels API optimisés
- **Configuration flexible** avec support multi-modèles Claude :
  - Claude 3.5 Sonnet (Recommandé)
  - Claude 3.5 Haiku (Rapide)
  - Claude 3 Opus (Puissant)
  - Claude 3 Sonnet
  - Claude 3 Haiku
- **Protocole MCP** pour accès aux données Odoo en temps réel
- **Interface Gradio** pour serveur MCP externe
- **Wizard chatbot** avec interface utilisateur intuitive
- **Contrôleur API REST** pour intégrations externes
- **Tests intégrés** pour validation de connexion
- **Gestion d'historique** des conversations
- **Architecture modulaire** respectant les bonnes pratiques Odoo 18.0

#### Sécurité
- Stockage sécurisé des clés API avec `password=True`
- Droits d'accès granulaires par modèle
- Validation des entrées utilisateur
- Gestion d'erreurs sans exposition de données sensibles

#### Documentation
- README complet avec guide d'installation
- Documentation de l'architecture
- Exemples d'utilisation
- Guide de dépannage
- Standards de contribution

#### Infrastructure
- Compatible Docker avec `docker-compose.yml`
- Configuration Odoo optimisée
- Support PostgreSQL
- Fichiers de sécurité Odoo appropriés

### 🔧 Technique

#### Architecture
```
MCP_Odoo/
├── models/
│   ├── anthropic_service.py     # Service API centralisé
│   ├── chatbot_config.py        # Configuration
│   ├── chatbot_wizard.py        # Interface utilisateur
│   └── chatbot_message.py       # Historique
├── controllers/
│   └── chatbot_controller.py    # API REST
├── views/
│   ├── chatbot_v18.xml         # Vues configuration
│   ├── chatbot_wizard_view.xml  # Vue chatbot
│   └── chatbot_messages.xml     # Vue messages
└── security/
    └── ir.model.access.csv      # Droits d'accès
```

#### Endpoints API
- `POST /api/chatbot/send_message` - Envoyer un message
- `GET /api/chatbot/get_messages` - Récupérer l'historique

#### Compatibilité
- **Odoo** : 18.0
- **Python** : 3.8+
- **PostgreSQL** : 12+
- **Docker** : 20.10+

---

## Format des versions

- **[Major.Minor.Patch]** - Date
- **Major** : Changements incompatibles
- **Minor** : Nouvelles fonctionnalités compatibles
- **Patch** : Corrections de bugs

## Types de changements

- **Ajouté** : Nouvelles fonctionnalités
- **Modifié** : Changements de fonctionnalités existantes
- **Déprécié** : Fonctionnalités bientôt supprimées
- **Supprimé** : Fonctionnalités supprimées
- **Corrigé** : Corrections de bugs
- **Sécurité** : Améliorations de sécurité 