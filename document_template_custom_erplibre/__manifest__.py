
{
    'name': 'document template custom erplibre',
    'author': 'TechnoLibre',
    'website': 'https://technolibre.ca',
    'category': 'Other',
    'description': """
document template custom erplibre
=================================

    """,
    'depends': [
        'account',
        'web',
        'sale',
    ],
    'data': [
        'views/report_invoice.xml',
        'views/report_templates.xml',
        'report/report_paperformat.xml',
        'data/report_layout.xml',
        'report/sale_report_templates.xml',
    ],
    "auto_install": False,
}
