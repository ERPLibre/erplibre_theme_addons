# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def get_theme_color(self, field_name='theme_color_primary'):
        theme_color_fields = [
            {'name': 'theme_color_brand', 'default': "#243742"},
            {'name': 'theme_color_primary', 'default': "#5D8DA8"},
            {'name': 'theme_color_required', 'default': "#d1dfe6"},
            {'name': 'theme_color_menu', 'default': "#f8f9fa"},
            {'name': 'theme_color_appbar_color', 'default': "#dee2e6"},
            {'name': 'theme_color_appbar_background', 'default': "#000000"},
        ]

        color_dict = next(field for field in theme_color_fields if field['name'] == field_name)
        default_color = color_dict['default']

        res = self.env['ir.config_parameter'].sudo().get_param(
            'muk_web_theme.{name}'.format(name=field_name), default=default_color)

        return res
