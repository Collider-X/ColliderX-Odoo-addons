# ColliderX-Odoo-addons
This repository contains Odoo modules that builds the infrastructure of ColliderX.

ColliderX currently runs on Odoo 11, so makes sure you're checking out the right branch (11.0).

## cx_operations
A module containing the configuration of Odoo for ColliderX, including company data, applications, and features.

## cx_website_theme
A module containing styling information. At this point it is only CSS, but it can contain more more.
More information on [Odoo's documentation](http://www.odoo.com/documentation/10.0/howtos/themes.html).

## cx_website
A module containing assets for the ColliderX website (i.e. web pages). It pulls styling automatically from `cx_website_theme`.

