from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    device_assignment_ids = fields.One2many('device.device.assignment', 'employee_id', string="Device Assignments")
    random_name = fields.Char(string="Random Name")