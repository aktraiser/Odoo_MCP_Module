# Mon Module Simple - Odoo V18

## Description

Ce module démontre la structure et les meilleures pratiques pour développer un module Odoo V18 simple et bien structuré. Il suit les conventions officielles d'Odoo et est conçu pour être facilement extensible.

## Fonctionnalités

- **Modèle de base** : Un modèle simple avec tous les champs essentiels
- **Workflow d'états** : Gestion des états (Brouillon → Confirmé → Terminé/Annulé)
- **Interface utilisateur** : Vues liste, formulaire et recherche complètes
- **Sécurité** : Permissions d'accès configurées
- **Tests unitaires** : Couverture complète des fonctionnalités
- **Données de démonstration** : Exemples pour tester le module

## Structure du Module

```
mon_module_simple/
├── __init__.py                 # Initialisation du module
├── __manifest__.py             # Métadonnées du module
├── README.md                   # Documentation
├── models/                     # Modèles de données
│   ├── __init__.py
│   └── mon_modele.py          # Modèle principal
├── views/                      # Vues XML
│   └── mon_modele_views.xml   # Vues du modèle
├── security/                   # Configuration de sécurité
│   └── ir.model.access.csv    # Permissions d'accès
├── data/                       # Données de base
│   └── mon_modele_data.xml    # Données initiales
├── demo/                       # Données de démonstration
│   └── mon_modele_demo.xml    # Exemples de données
└── tests/                      # Tests unitaires
    ├── __init__.py
    └── test_mon_modele.py     # Tests du modèle
```

## Installation

### Prérequis

- Odoo V18
- Python 3.8+
- PostgreSQL

### Installation avec Docker

1. Clonez ce module dans votre dossier addons Odoo
2. Redémarrez votre instance Odoo
3. Activez le mode développeur
4. Allez dans Apps → Mettre à jour la liste des apps
5. Recherchez "Mon Module Simple" et installez-le

### Installation manuelle

1. Copiez le dossier `mon_module_simple` dans votre répertoire addons
2. Ajoutez le chemin dans votre configuration Odoo
3. Redémarrez le service Odoo
4. Installez le module depuis l'interface

## Utilisation

### Accès au module

Après installation, le module est accessible via :
- **Menu principal** : Mon Module → Mon Modèle

### Fonctionnalités principales

1. **Création d'enregistrements** : Cliquez sur "Créer" pour ajouter un nouvel élément
2. **Gestion des états** : Utilisez les boutons dans l'en-tête pour changer l'état
3. **Filtres et recherche** : Utilisez la barre de recherche pour filtrer les enregistrements
4. **Priorités** : Définissez la priorité avec le widget étoiles

### Workflow des états

- **Brouillon** → **Confirmé** → **Terminé**
- **Brouillon** → **Annulé**
- Possibilité de remettre en brouillon depuis n'importe quel état

## Développement

### Bonnes pratiques implémentées

1. **Structure modulaire** : Séparation claire des responsabilités
2. **Nommage cohérent** : Conventions Odoo respectées
3. **Documentation** : Code bien documenté avec docstrings
4. **Validation** : Contraintes et validations appropriées
5. **Sécurité** : Permissions configurées correctement
6. **Tests** : Couverture de test complète
7. **Internationalisation** : Chaînes traduisibles marquées

### Extension du module

Pour étendre ce module :

1. **Ajouter des champs** : Modifiez `models/mon_modele.py`
2. **Nouvelles vues** : Créez des fichiers XML dans `views/`
3. **Permissions** : Mettez à jour `security/ir.model.access.csv`
4. **Tests** : Ajoutez des tests dans `tests/`

### Tests

Exécuter les tests :

```bash
# Tests unitaires
odoo-bin -d test_db -i mon_module_simple --test-enable --stop-after-init

# Tests spécifiques
odoo-bin -d test_db --test-tags mon_module_simple
```

## Configuration

### Paramètres par défaut

- **État initial** : Brouillon
- **Priorité par défaut** : Normal
- **Utilisateur responsable** : Utilisateur connecté
- **Archivage** : Activé par défaut

### Personnalisation

Le module peut être personnalisé via :
- Héritage des modèles
- Extension des vues XML
- Ajout de nouveaux champs
- Modification des workflows

## Dépendances

- `base` : Module de base Odoo (requis)

## Licence

LGPL-3 - Voir le fichier LICENSE pour plus de détails

## Support

Pour toute question ou problème :
- Consultez la documentation Odoo officielle
- Vérifiez les logs Odoo pour les erreurs
- Testez en mode développeur

## Changelog

### Version 18.0.1.0.0
- Version initiale
- Modèle de base avec workflow d'états
- Vues complètes (liste, formulaire, recherche)
- Tests unitaires
- Documentation complète

## Auteur

Développé selon les meilleures pratiques Odoo V18 