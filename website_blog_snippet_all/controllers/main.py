from odoo import http
from odoo.http import request


class WebsiteBlogSnippetAllController(http.Controller):
    @http.route(
        ["/website_blog_snippet_all/helloworld"],
        type="json",
        auth="public",
        website=True,
        methods=["POST", "GET"],
        csrf=False,
    )
    def hello_world(self):
        return {"hello": "Hello World!"}