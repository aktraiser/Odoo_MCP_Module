{
    'name': 'Chatbot Custom MCP',
    'version': '1.0',
    'summary': 'Module de base pour un chatbot Odoo avec MCP Gradio',
    'description': 'Permet la gestion de messages pour un chatbot personnalisé connecté à l\'API Anthropic via MCP Gradio.',
    'author': 'Lucas Bometon',
    'website': 'https://github.com/lucasbometon',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/chatbot_v18.xml',
        'views/chatbot_messages.xml',
        'views/chatbot_wizard_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mon_module_simple/static/src/scss/chatbot_modal.scss',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
} 