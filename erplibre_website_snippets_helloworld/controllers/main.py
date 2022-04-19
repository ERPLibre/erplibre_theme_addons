from odoo import http


class WebsiteDonationMeter(http.Controller):
    @http.route(['/website_helloworld/get_message/'], type="json",
                auth="public", website=True)
    def get_message(self):
        return {"message":"Hello super world"}

