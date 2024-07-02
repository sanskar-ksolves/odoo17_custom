from odoo import fields , models , api

class DeviceAttributeValue(models.Model):
    _name = 'device.device.attributes.value'
    _description = 'About Attributes Value'

    name = fields.Char(string='Name',required=True)
    device_model_ids = fields.Many2many('device.device.attribute', 'device_model_device_attributes_value_rel', 'device_attribute_value_id','device_model_id', string='Device Model')
