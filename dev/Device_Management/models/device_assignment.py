from odoo import fields, models, api

class DeviceAssignment(models.Model):
    _name = "device.device.assignment"
    _description = "Device assignment details"
    _rec_name = 'name'

    name = fields.Char(string="Name", required=True)
    device_id = fields.Many2one('device.device', string="Device", required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    date_start = fields.Date(string="Start Date", required=True)
    date_expired = fields.Date(string="Expire Date")
    state = fields.Selection([
        ('new', 'New'),
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('returned', 'Returned'),
        ('rejected', 'Rejected'),
    ], string="State", default='new')

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Choose another value - Name should be unique!')
    ]


    @api.model
    def create(self, vals):
        if 'name' not in vals or not vals['name']:
            vals['name'] = self.env['ir.sequence'].next_by_code('device.assignment')
        return super(DeviceAssignment, self).create(vals)

    def action_draft(self):
        self.state = 'draft'

    def action_approve(self):
        self.state = 'approved'

    def action_return(self):
        self.state = 'returned'

    def action_reject(self):
        self.state = 'rejected'
