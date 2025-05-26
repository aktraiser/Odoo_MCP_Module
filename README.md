# Module Odoo Simple - Workflow Manager

Un module Odoo 18.0 simple démontrant les meilleures pratiques de développement selon la documentation officielle.

## 🚀 Fonctionnalités

- ✅ **Structure modulaire** conforme aux standards Odoo 18.0
- ✅ **Vues modernes** : Liste, Kanban et Formulaire
- ✅ **Interface utilisateur** intuitive avec boutons d'action
- ✅ **Gestion d'états** avec workflow simple
- ✅ **Champs calculés** et validations
- ✅ **Sécurité** avec droits d'accès appropriés
- ✅ **Docker** pour un déploiement facile

## 📋 Prérequis

- Docker
- Docker Compose
- Git

## 🛠️ Installation

1. **Cloner le repository**
```bash
git clone <votre-repo-url>
cd Odoo_workflow
```

2. **Démarrer les conteneurs**
```bash
docker-compose up -d
```

3. **Accéder à Odoo**
- URL : http://localhost:8069
- Utilisateur : `admin`
- Mot de passe : `admin`

## 📁 Structure du Projet

```
Odoo_workflow/
├── docker-compose.yml          # Configuration Docker
├── odoo.conf                   # Configuration Odoo
├── mon_module_simple/          # Module principal
│   ├── __init__.py
│   ├── __manifest__.py         # Manifest du module
│   ├── models/                 # Modèles de données
│   │   ├── __init__.py
│   │   └── mon_modele.py
│   ├── views/                  # Vues XML
│   │   └── mon_modele_views.xml
│   ├── security/               # Droits d'accès
│   │   └── ir.model.access.csv
│   ├── data/                   # Données par défaut
│   │   └── mon_modele_data.xml
│   ├── demo/                   # Données de démonstration
│   │   └── mon_modele_demo.xml
│   └── static/description/     # Ressources statiques
│       └── icon.png
└── README.md
```

## 🎯 Utilisation

### Accès au Module

1. Connectez-vous à Odoo
2. Recherchez "Mon Module" dans le menu principal
3. Cliquez sur "Mon Modele" pour accéder aux fonctionnalités

### Fonctionnalités Disponibles

- **Vue Liste** : Affichage tabulaire avec colonnes personnalisées
- **Vue Kanban** : Affichage en cartes avec informations visuelles
- **Création** : Bouton "NEW" pour créer de nouveaux enregistrements
- **Workflow** : États (Brouillon → Confirmé → Terminé)
- **Filtres** : Recherche et filtrage avancés

## 🔧 Développement

### Commandes Utiles

```bash
# Redémarrer Odoo
docker-compose restart odoo

# Voir les logs
docker-compose logs odoo

# Mettre à jour le module
docker-compose restart odoo

# Arrêter les conteneurs
docker-compose down

# Supprimer les volumes (reset complet)
docker-compose down -v
```

### Modifications du Code

1. Modifiez les fichiers dans `mon_module_simple/`
2. Redémarrez le conteneur Odoo
3. Les changements sont automatiquement pris en compte

## 📚 Documentation

Ce module suit les [directives de codage officielles d'Odoo 18.0](https://www.odoo.com/documentation/18.0/fr/contributing/development/coding_guidelines.html) :

- **Conventions de nommage** : Préfixes appropriés pour les IDs XML
- **Structure des vues** : Utilisation de `<list>` au lieu de `<tree>`
- **Widgets modernes** : `badge`, `boolean_toggle`, `statusbar`
- **Sécurité** : Droits d'accès granulaires
- **Performance** : Champs calculés avec `@api.depends`

## 🐛 Dépannage

### Le module n'apparaît pas
1. Vérifiez que `'application': True` dans `__manifest__.py`
2. Vérifiez que les vues sont incluses dans la section `'data'`
3. Redémarrez le conteneur

### Erreurs de base de données
```bash
docker-compose down -v
docker-compose up -d
```

### Logs d'erreur
```bash
docker-compose logs odoo | grep -i error
```

## 🤝 Contribution

1. Fork le projet
2. Créez une branche feature (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence LGPL-3. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

Votre Nom - [votre-email@example.com]

## 🙏 Remerciements

- [Documentation officielle Odoo](https://www.odoo.com/documentation/18.0/)
- [Communauté Odoo](https://www.odoo.com/forum)
- [Docker](https://www.docker.com/) 