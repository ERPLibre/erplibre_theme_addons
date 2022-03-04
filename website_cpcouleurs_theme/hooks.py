import os
import sys
from odoo import SUPERUSER_ID, _, api, fields, models, http

# Add path to call function in controller web_editor
# new_path = os.path.normpath(
#     os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '..', 'odoo', 'addons', 'web_editor'))
# sys.path.append(new_path)
# from controllers import main as web_editor_controllers_main
from odoo.http import controllers_per_module
from odoo.addons.web_editor.controllers.main import Web_Editor


def post_init_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        # Source: odoo/addons/web_editor/controllers/main.py

        # controller_instance = None
        for name, instance in controllers_per_module.get("web_editor"):
            if name == "odoo.addons.web_editor.controllers.main.Web_Editor":
                controller_instance = instance()
                break
        if controller_instance is not None:
            #     controller_instance.snippets()
            # web_editor = web_editor_controllers_main.Web_Editor()
            # print(web_editor)
            views_1 = env["ir.ui.view"].get_related_views('website.homepage')
            views = views_1.read(controller_instance._get_view_fields_to_read())
            custom_url = controller_instance._make_custom_scss_file_url("%%.%%", "%%")
            IrAttachment = env["ir.attachment"]
            attachment = IrAttachment.search([("url", "=like", custom_url)])
            print("yeah")
