from odoo import http


class WebsiteDonationMeter(http.Controller):
    @http.route(['/website_helloworld/get_message/'],
                auth="public", website=True)
    def get_message(self):
        return "Hello super world"

