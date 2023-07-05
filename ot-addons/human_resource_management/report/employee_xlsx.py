from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.human_resource_management.report_xlsx_employee'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, employees):
        sheet = workbook.add_worksheet('Employee details')
        bold = workbook.add_format({'bold': True})
        format1 = workbook.add_format({'font_size': 12, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'center'})
        row = 0
        col = 0
        sheet.set_column('D:D', 12)
        sheet.write(row, col, 'First Name', format1)
        sheet.write(row + 1, col, 'Last Name', format1)
        sheet.write(row + 2, col, 'Age', format1)
        sheet.write(row + 3, col, 'Currency ', format1)
        sheet.write(row + 4, col, 'Salary', format1)

        sheet.write(row, col + 1, employees.name, format2)
        sheet.write(row + 1, col + 1, employees.last_name, format2)
        sheet.write(row + 2, col + 1, employees.age, format2)
        sheet.write(row + 3, col + 1, employees.currency_id.name, format2)
        sheet.write(row + 4, col + 1, employees.salary, format2)

        col += 3
        sheet.write(row, col, 'Address ', format1)
        sheet.write(row + 1, col, 'Region', format1)
        sheet.write(row + 2, col, 'Nationality', format1)
        sheet.write(row + 3, col, 'Type of work  ', format1)

        sheet.write(row, col + 1, employees.address, format2)
        sheet.write(row + 1, col + 1, employees.region_id.name, format2)
        sheet.write(row + 2, col + 1, employees.nationality, format2)
        sheet.write(row + 3, col + 1, employees.type_of_work, format2)

        row += 7
        col = 0
        sheet.write(row, col, 'Name ', format1)
        sheet.write(row, col + 1, 'Date ', format1)
        sheet.write(row, col + 2, 'Phone ', format1)
        appointments = employees.mapped('appointment_ids')
        for appointment in appointments:
            if appointment.type == 'new':
                sheet.write(row + 1, col, appointment.new_beneficiary_name, format2)
            else:
                sheet.write(row + 1, col, appointment.beneficiary_id.name, format2)
            sheet.write(row + 1, col + 1, appointment.appointment_datetime, format2)
            sheet.write(row + 1, col + 2, appointment.phone_number, format2)
            row += 1
