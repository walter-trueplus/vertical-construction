# -*- coding: utf-8 -*-

from odoo import models, fields


class Project(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    architect = fields.Many2one('res.partner',
                                domain="[('isArchitect', '=', '1')]")
