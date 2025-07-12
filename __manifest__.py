{
    'name': 'StackIt Forum',
    'version': '1.0',
    'summary': 'Minimal Q&A forum platform for Odoo Hackathon',
    'author': 'Harsh Bhanushali',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/question_views.xml',
        'views/answer_views.xml',
        'views/tag_views.xml',
        'views/vote_views.xml',
        'views/notification_views.xml',
        'views/dashboard_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # optional JS/CSS later
        ],
    },
    'images': ['static/description/icon.svg'],
    'installable': True,
    'application': True,
}
