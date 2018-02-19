# -*- encoding: utf-8 -*-
#	The ColliderX website module (cx_website) is an Odoo module that packs the ColliderX web assets on top of the base Odoo 11 community version.
#	Copyright (C) 2017 Marc Lijour
#   https://www.linkedin.com/in/marclijour
#   https://github.com/Collider-X/ColliderX-Odoo-addons/cx_website
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
    'name': "ColliderX Website",

    'summary': """
        This module packs the ColliderX web assets on top of the base Odoo 11 community version.
        It's an optional add-on to the ColliderX application (cx_operations).""",

    'description': """
        The ColliderX Website includes static pages, menu configuration items, and styling.
        Note: the theme assets are called from the companion module (cx_website_theme).
    """,

    'author': "Marc Lijour",
    'website': "https://www.linkedin.com/in/marclijour/",
    'license': "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
				'website', 'website_mass_mailing',  # 2nd is for newsletter subscription
                'cx_website_theme', # ColliderX theme in a companion module
				#'theme_default',	# we need the plain bootstrap theme (on the community edition CE)
                'web_enterprise',   # incompatible with theme_default
				],

    # always loaded
    'data': [
        'pages/homepage.xml',
        'pages/footer.xml',
        'pages/donate.xml',
    ],

    "auto_install": False,
    "installable": True,
}

