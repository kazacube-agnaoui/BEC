# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "BEC CHANTIERS",
    "author": "KAZACUBE-ABDELLATIF BENZBIRIA",
    "website": "www.kazacube.com",
    "description": """
This module allow to manage demolition site
    """,
    "version": "1.0",
    "category": "Site & Sales & Purchases & Stock",
    "depends": [
        "sale","purchase",
    ],
    "data": [
         "site_view.xml",
    ],
    "installable": True,
}