# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Mathias Colpaert
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
    'name': "OCA Construction: Project Architect",
    'summary': """Indicate the architect of a project.""",
    'description': """
        This module allows you to:
            - Identify the architect of a project.
            - Filter/group/search projects by architect.
    """,
    'author': "Mathias Colpaert,Odoo Community Association (OCA)",
    'category': "construction",
    'version': '11.0.0',
    'depends': ['project', 'base_construction_architect'],
    'data': ['views.xml'],
    'installable': False,
}
