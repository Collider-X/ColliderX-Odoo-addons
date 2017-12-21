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

{
    'name': "ColliderX Main Application",

    'summary': """
        This module contains the ColliderX configuration data and apps for Odoo 11.
    """,

    'description': """
        This module contains the ColliderX configuration data and apps for Odoo 11.
        
        Other companion modules can be installed separately: 
            * the ColliderX Website includes static pages, and menu configuration items
            * the ColliderX Website Theme includes only the theme (CSS, Javascript)
    """,

    'author': "Marc Lijour",
    'website': "https://www.linkedin.com/in/marclijour/",
    'license': "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'l10n_ca',      # base Odoo and Canadian context (incl. accounting)
				'website', 
				'theme_default',	    # we need the plain bootstrap theme
                'auth_signup',          # allows user to self-register
                'membership',           # to manage memberships
                'website_crm',          # adds contact form, and pulls in crm, website_form, website_partner
                'website_sale',         # pulls in 'sale', 'website', 'payment', etc
                'payment_stripe',       # pulls in 'payment'
                'account_invoicing',    # 
				],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv', TODO later
        'views/set_config_parameters.xml',  # programmatically set config parameters (company, data, favicon, config, etc)
        'views/signup_member.xml',          # tailors the auth_signup form HTML for ColliderX needs
        'views/extended-res_partner_form.xml',    # to display the information from the members panel in Odoo
        'views/extended-res_users_form.xml',    # to display the first name and last name separately under the full name on the users panel
    ],

    "auto_install": False,
    "installable": True,
}

