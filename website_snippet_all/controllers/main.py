from odoo import http
from odoo.http import request


class WebsiteSnippetAllController(http.Controller):
    @http.route(
        ["/website_snippet_all/helloworld"],
        type="json",
        auth="public",
        website=True,
        methods=["POST", "GET"],
        csrf=False,
    )
    def hello_world(self):
        return {"hello": "Hello World!"}
