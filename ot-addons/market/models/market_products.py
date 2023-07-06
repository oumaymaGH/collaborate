from odoo import models,api,fields

class MarketProducts(models.Model):
    _name="market.products"

    name=fields.Char(string="Product Name")
    state = fields.Selection([('buy', 'Buy'), ('sell', 'Sell')],default='buy')

    message=fields.Text(string="Message")
    def function_test(self):
        for rec in self :
         if rec.state=='buy':
            rec.name="Amina"
            print(rec.name)