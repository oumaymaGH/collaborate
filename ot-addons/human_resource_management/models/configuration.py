from odoo import models, api, fields


class TypeOfWork(models.Model):
    _name = "work.type"
    name = fields.Char(string="Name")
