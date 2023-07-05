from odoo import api, fields, models


class Region(models.Model):
    _name = "sanabel.region"
    name = fields.Char(string="Name")



class Investigator(models.Model):
    _name = "sanabel.investigator"
    name = fields.Char(string="Name")
