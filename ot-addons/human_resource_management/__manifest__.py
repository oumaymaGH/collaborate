{
    'name': 'H-Resource Management',
     'author':'Author',
    'depends': [
        'base', 'appointment','report_xlsx'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/appointment.xml',
        'views/employee.xml',
        'views/menu.xml',
        'report/report.xml',
        'report/employee_report.xml',
        'report/employee_xlsx.xml'

    ],
    'application': True,
}
