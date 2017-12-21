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


from odoo import models, fields, api

import os

import logging
_logger = logging.getLogger(__name__)

# To add first name and last name to the person record
# note. res.users (reserved for technical data) inherits from res.partner
class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_firstname = fields.Char(
        string="First Name",             # Optional label of the field
        help='A person\' first name',    # Help tooltip text
    )

    x_lastname = fields.Char(
        string="Last Name",             # Optional label of the field
        help='A person\' last name',    # Help tooltip text
    )

