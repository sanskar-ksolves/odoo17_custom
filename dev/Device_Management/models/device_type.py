from odoo import fields , models , api
from datetime import  date,datetime


class DeviceType(models.Model):
    _name = 'device.device.type'
    _description = 'Information about device types.'

    name = fields.Char(string="Name",required=True)
    code = fields.Char(string="Code",required=True)
    sequence = fields.Char(string='Sequence')
    device_attr_ids = fields.Many2many('device.device.attribute','device_attr_device_type_rel','device_type_id','device_attributes_id',string='Device Attributes')
    device_model_ids = fields.Many2many('device.device.model','device_model_device_type_rel','device_type_id','device_model_id',string='Device Model')
    device_ids = fields.Many2many('device.device', 'device_type_device_rel','device_type_id','device_id',string='Devices')

    _sql_constraints = [
        ('unique_code',
         'unique(code)',
         'Choose another value - Code should ve unique!'),

        ('unique_name',
         'unique(name)',
         'Choose another value - Name should be unique!')
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            code = self.env['ir.sequence'].next_by_code(
                'device.device.type') or False
            vals['sequence'] = 'DA' + str(datetime.now().strftime("%y")) + '/' + str(code)

        return super().create(vals_list)