from odoo import models, fields

class StackTag(models.Model):
    _name = 'stackit.tag'
    _description = 'Forum Tag'

    name = fields.Char(required=True)
    color = fields.Integer(string="Color Index", default=0)
