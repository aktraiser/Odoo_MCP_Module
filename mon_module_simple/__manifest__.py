{
    'name': 'Mon Module Simple',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Un module Odoo simple suivant les meilleures pratiques',
    'description': """
        Module Odoo V18 Simple
        ======================
        
        Ce module démontre la structure de base d'un module Odoo V18
        en suivant les meilleures pratiques de développement.
        
        Fonctionnalités:
        - Structure modulaire claire
        - Modèle de base avec champs essentiels
        - Vues XML héritées
        - Sécurité et permissions
        - Tests unitaires
    """,
    'author': 'Votre Nom',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/mon_modele_views.xml',
        'data/mon_modele_data.xml',
    ],
    'demo': [
        'demo/mon_modele_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
} 