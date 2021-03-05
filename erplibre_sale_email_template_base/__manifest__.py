
{
    'name': 'ERPLibre Sale Email Template Base',
    'author': 'TechnoLibre',
    'website': 'https://technolibre.ca',
    'category': 'Other',
    'description': 'Base module for email template. Exposing the color variables for template styling',
    'depends': [
        'mail',
        'sale',

        # Muk
        'muk_web_theme',
    ],
    'data': [
        'data/mail_data.xml',
    ],
    "auto_install": False,
}
