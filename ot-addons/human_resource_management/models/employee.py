from odoo import api, fields, models


class EmployeeManagement(models.Model):
    _name = "employee.management"
    name = fields.Char(string="First Name",required=True)
    last_name = fields.Char(string="Last Name",required=True)
    age = fields.Integer(string="Age",required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.ref('base.LBP').id)
    salary = fields.Monetary(string='Salary', currency_field='currency_id')
    # type_of_work_ids = fields.Many2many('work.type', string="Type of work")
    type_of_work = fields.Selection([('investigator', 'Investigator'),
                                     ('field_visit', 'Field Visit'),
                                     ('it', 'IT'), ('logistic', 'Logistic'),
                                     ('accounting', 'Accounting')
                                     ], string="Type of Work",required=True)
    address = fields.Char(string="Address")
    region_id = fields.Many2one('sanabel.region', string="Region")
    nationality = fields.Selection([('lebanese', 'Lebanese'), ('syrian', 'Syrian')])
    appointment_ids = fields.One2many('sanabel.appointment', 'employee_id', string="Appointments")
    manager = fields.Many2one(comodel_name='employee.management', string="Manager",
                              domain="[('type_of_work', '=', type_of_work)]")

    # @api.depends('name')
    # def _compute_appointments(self):
    #     for record in self:
    #         record.appointment_ids = self.env['sanabel.appointment'].search(
    #             [('investigator_id', '=', record.name)])
