from odoo import fields , models , api

class DeviceAttributeAssignment(models.Model):
    _name = 'device.device.attribute.assignment'
    _description = 'About Attributes Value'
    _rec_name = 'device_id'


    device_id = fields.Char(string='Device')
    device_attribute_id = fields.Many2one('device.device.attribute',  string='Device Attribute')
