
from odoo import http, tools, _
from odoo.addons.website_sale.controllers.main import WebsiteSale

class MyWebsiteSale(WebsiteSale):

    def _get_mandatory_billing_fields(self):
        return ["name", "email"]

