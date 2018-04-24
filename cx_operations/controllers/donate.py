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

import werkzeug
import requests

import logging
_logger = logging.getLogger(__name__)

class Donate(http.Controller):
    # Identifies the right donation product to link to 
    # parameters: a currency and a category
    # returns: product_id of the donation/product
    @http.route('/cx/product_id', type='http', auth='none', methods=['POST', 'GET'], website=True, csrf=False)
    def get_product_id(self, currency, category, **kw):
        category = category.replace('"', '')
        #_logger.info("currency={}".format(currency))
        #_logger.info("category={}".format(category))
        public = request.env.ref('base.public_user')    # env restricted to public user
        product_id = "unknown"
        #_logger.info("query={}".format('%{cat}%{cur}%'.format(cat=category,cur=currency)))
        product = request.env['product.product'].sudo(public).search([('name', '=like', '%{cat}%{cur}%'.format(cat=category,cur=currency))])
        if product.__len__() > 0:
            product_id = product[0].id 
        _logger.info("product: %s", product)
        return str(product_id)

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
        ### 
        _logger.info("### qty=%s", amount)
        _logger.info("### product_id=%s", product_id)
        # apparently there is no forward fonction in Odoo/Werkzeug, so doing this manually
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url', default='')
        target_url = base_url + '/shop/cart/update'
        result = requests.post(target_url, data=values)
        _logger.info('### result url=%s', target_url)
        return Response(result)

#        href = werkzeug.Href(request.env['ir.config_parameter'].sudo().get_param('web.base.url', default=''))
#        _logger.info(href('/shop/cart/update', values))
#        return request.redirect(href('/shop/cart/update', values))

#        _logger.info("### user_id=%s", request.website.user_id)
#        _logger.info("### partner_id=%s", request.website.user_id.sudo().partner_id)
#        # code from website_sale/controllers/main.py route:/shop/cart/update
#        add_qty=0 # TODO test
#        partner_id = request.website.user_id.sudo().partner_id
#        _logger.info('### partner_id=%s', partner_id)
#        ###
#        _logger.info("### order=%s", request.website.sale_get_order)
##        _logger.info("### partner in order=%s", request.website.sale_get_order.partner_id)
#        request.website.sale_get_order(force_create=1)._cart_update(
#            product_id=int(product_id),
#            add_qty=add_qty,
#            set_qty=amount,
#            attributes=self._filter_attributes(**kw),
#        )
#        ###
#        _logger.info("### order=%s", request.website.sale_get_order)
#        return request.redirect("/shop/cart")


