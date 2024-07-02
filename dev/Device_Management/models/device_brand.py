from odoo import fields , models , api

class DeviceBrand(models.Model):
    _name = 'device.device.brand'
    _description = 'About device brand'

    name = fields.Char(string='Name',required=True)
    device_model_ids = fields.Many2many('device.device.model', 'device_model_device_brand_rel', 'device_brand_id',
                                        'device_model_id', string='Device Model')
