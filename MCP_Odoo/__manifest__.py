{
    'name': 'Chatbot Custom MCP',
    'version': '1.1.0',
    'summary': 'Module chatbot Odoo moderne avec MCP Gradio et historique',
    'description': '''
    Module de chatbot Odoo avec interface moderne incluant :
    • Interface de chat moderne avec bulles de messages
    • Historique des conversations par utilisateur
    • Interactivité JavaScript avancée
    • Styles CSS modernes et responsifs
    • Intégration API Anthropic via MCP Gradio
    • Gestion des sessions et traçabilité
    ''',
    'author': 'Lucas Bometon',
    'website': 'https://github.com/lucasbometon',
    'category': 'Tools',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/chatbot_v18.xml',
        'views/chatbot_wizard_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'MCP_Odoo/static/src/scss/chatbot_modal.scss',
            'MCP_Odoo/static/src/js/chatbot_widget.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 