# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PortalMixin(models.AbstractModel):
    _inherit = "portal.mixin"

    def get_theme_color_brand(self):
        result = self.env['ir.config_parameter'].sudo().get_param(
            'muk_web_theme.theme_color_brand', default='')
        return result

    def get_theme_color_primary(self):
        result = self.env['ir.config_parameter'].sudo().get_param(
            'muk_web_theme.theme_color_primary', default='')
        return result

    def get_theme_color_required(self):
        result = self.env['ir.config_parameter'].sudo().get_param(
            'muk_web_theme.theme_color_required', default='')
        return result

    def get_theme_color_menu(self):
        result = self.env['ir.config_parameter'].sudo().get_param(
            'muk_web_theme.theme_color_menu', default='')
        return result

    def get_theme_color_appbar_color(self):
        result = self.env['ir.config_parameter'].sudo().get_param(
            'muk_web_theme.theme_color_appbar_color', default='')
        return result

    def get_theme_color_appbar_background(self):
        result = self.env['ir.config_parameter'].sudo().get_param(
            'muk_web_theme.theme_color_appbar_background', default='')
        return result
