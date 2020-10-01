
{
    'name': 'invoice template custom erplibre',
    'author': 'TechnoLibre',
    'website': 'https://technolibre.ca',
    'category': 'Other',
    'description': """
invoice template custom erplibre
================================

    """,
    'depends': [
        'account',
        'web',
        'sale',
        'mail',
    ],
    'data': [
        'views/report_invoice.xml',
        'views/report_templates.xml',
        'data/report_layout.xml',
        'report/sale_report_templates.xml',
        'data/mail_data.xml',
    ],
    "auto_install": False,
}
