from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AppointmentInheritance(models.Model):
    _inherit = "sanabel.appointment"
    employee_id = fields.Many2one('employee.management', string="Investigator",
                                  domain="[('type_of_work', '=','investigator')]")

    @api.model
    def create(self, vals):
        existing_appointments = self.env['sanabel.appointment'].search(
            [('employee_id', '=', vals['employee_id']),
             ('appointment_datetime', '=', vals['appointment_datetime'])])
        if existing_appointments:
            raise ValidationError("You already have an  appointment in the same time")
        else:
            return super().create(vals)
