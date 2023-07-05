from odoo import api, fields, models


class Beneficiary(models.Model):
    _name = "sanabel.beneficiary"
    name = fields.Char(string="Name")
    number_of_children = fields.Integer(string="Number of children ")
    region_id = fields.Many2one('sanabel.region', "Region")
    phone_number = fields.Char(string="Phone Number",required=True)
    nationality = fields.Selection([('lebanese', 'Lebanese'), ('syrian', 'Syrian')])

