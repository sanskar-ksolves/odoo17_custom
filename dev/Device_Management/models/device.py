from odoo import fields, models, api

class Device(models.Model):
    _name = "device.device"
    _description = "Device details"
    _rec_name = 'name'


    name = fields.Char(string="Name", required=True)
    shared = fields.Boolean(string="Shared")
    device_type_id = fields.Many2one('device.device.type', string="Device Type")
    device_brand_id = fields.Many2one('device.device.brand', string="Device Brand")
    device_model_id = fields.Many2one('device.device.model', string="Device Model")
    attributes = fields.Many2many('device.device.attribute', 'device_attributes_rel', 'attributes_id', 'device_id', string="Device Attributes Assignments")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Choose another value - Name should be unique!')
    ]
