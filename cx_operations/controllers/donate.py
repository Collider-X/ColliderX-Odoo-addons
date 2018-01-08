# -*- encoding: utf-8 -*-
#	The ColliderX main module (cx_operations) contains the ColliderX configuration data and apps for Odoo 11 (community).
#	Copyright (C) 2017 Marc Lijour
#   https://www.linkedin.com/in/marclijour
#   https://github.com/Collider-X/ColliderX-Odoo-addons/tree/11.0
#
#	This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

from odoo import http
from odoo.http import request, Response

import requests

import logging
_logger = logging.getLogger(__name__)

class Donate(http.Controller):
    # Gets information from the simple form on the donate page (GET)
    # and sets up the shopping cart with the proper amount (int) and currency (code e.g. USD)
    @http.route('/cx/donate', type='http', auth='none', methods=['POST'], website=True, csrf=False)
    def set_shopping_cart(self, amount, currency, **kw):
        # fetch product id <-> donation of 1 unit of the chosen currency
        public = request.env.ref('base.public_user')    # env restricted to public user
        product_id = request.env['product.template'].sudo(public).search([('name', '=like', '%{}%'.format(currency))]).id
        values = {
            'set_qty': amount, 
            'product_id': product_id
        }
        # apparently there is no forward fonction in Odoo/Werkzeug, so doing this manually
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url', default='')
        target_url = base_url + '/shop/cart/update'
        result = requests.post(target_url, data=values)
        return Response(result)

