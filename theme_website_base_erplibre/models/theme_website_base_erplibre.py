from odoo import _, api, fields, models


class ThemeWebsiteBaseErplibre(models.AbstractModel):
    _inherit = "theme.utils"

    def _theme_website_base_erplibre_post_copy(self, mod):
        self.disable_view("website_theme_install.customize_modal")
