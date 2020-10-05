# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    theme_color_brand = fields.Char(
        string="Theme Brand Color")

    theme_color_primary = fields.Char(
        string="Theme Primary Color")

    theme_color_required = fields.Char(
        string="Theme Required Color")

    theme_color_menu = fields.Char(
        string="Theme Menu Color")

    theme_color_appbar_color = fields.Char(
        string="Theme AppBar Color")

    theme_color_appbar_background = fields.Char(
        string="Theme AppBar Background")

    @api.multi
    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('email_template_custom_erplibre.theme_color_brand', self.theme_color_brand)
        param.set_param('email_template_custom_erplibre.theme_color_primary', self.theme_color_primary)
        param.set_param('email_template_custom_erplibre.theme_color_required', self.theme_color_required)
        param.set_param('email_template_custom_erplibre.theme_color_menu', self.theme_color_menu)
        param.set_param('email_template_custom_erplibre.theme_color_appbar_color', self.theme_color_appbar_color)
        param.set_param('email_template_custom_erplibre.theme_color_appbar_background', self.theme_color_appbar_background)
        return res

