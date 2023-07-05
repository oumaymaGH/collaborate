from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Appointment(models.Model):
    _name = "sanabel.appointment"
    name = fields.Char(string="Appointment Record")
    type = fields.Selection([('new', 'New'), ('renew', 'Renew')], default='new')
    # phone_number = fields.Char(string="Phone", compute='_compute_phone_number')
    phone_number = fields.Char(string="Phone")
    appointment_datetime = fields.Datetime(string="Appointment Time")
    beneficiary_id = fields.Many2one('sanabel.beneficiary', "Old Beneficiary Name")
    new_beneficiary_name = fields.Char(string="New Beneficiary Name")
    region_id = fields.Many2one('sanabel.region', "Region")
    investigator_id = fields.Many2one('sanabel.investigator', "Investigators",required=True)
    state = fields.Selection([('opened', 'Opened'), ('done', 'Done'), ('rejected', 'Rejected')], default='opened')


    @api.model
    def create(self, vals):
        existing_appointments = self.env['sanabel.appointment'].search([])
        for record in existing_appointments:
            if (record.new_beneficiary_name == vals['new_beneficiary_name'] or record.beneficiary_id == vals[
                'beneficiary_id']) and record.state == "opened":
                raise ValidationError("You already have an opened appointment")
        return super().create(vals)

    @api.onchange('beneficiary_id')
    def onchange_beneficiary_id(self):
        self.phone_number = self.beneficiary_id.phone_number
        self.region_id = self.beneficiary_id.region_id

    @api.ondelete(at_uninstall=False)
    def _ondelete_function(self):
        for record in self:
            if record.state in ['done', 'rejected']:
                raise ValidationError("You can't delete this appointment because it's not pending.")

    def write(self, values):
        if self.state in ['done', 'rejected']:
            raise ValidationError("You can not Edit on this because it is not pending")
            return False

        return super(Appointment, self).write(values)

    def action_button_reopen(self):
        if self.state != 'opened':
            self.state = 'opened'
        else:
            raise ValidationError("It is already Opened")

    def action_button_reject(self):
        if self.state != 'rejected':
            self.state = 'rejected'
        else:
            raise ValidationError("It is already Rejected")

    def action_button_done(self):
        if self.state != 'done':
            self.state = 'done'
        else:
            raise ValidationError("It is already Done")

    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.state = 'opened'

    @api.onchange('name')
    def _onchange_for_phone(self):
        if self.type == 'renew':
            self.phone_number = self.beneficiary_id.phone_number
