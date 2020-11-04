# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        values = {
            # set default paperformat to custom one
            'paperformat_id': env.ref("document_template_custom_erplibre.paperformat_custom_erplibre").id
        }
        print(values['paperformat_id'])
        event_config = env['res.config.settings'].sudo().create(values)
        event_config.execute()
