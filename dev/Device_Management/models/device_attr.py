from odoo import  fields,models,api

class DeviceAttribute(models.Model):
    _name = "device.device.attribute"
    _description = """
                    Device attributes details 
                   """
    name = fields.Char(string="Name", required=True)
    required = fields.Boolean(string="Required")
    device_type_id = fields.Many2one('device.device.type',string="Device Type")
    device_value_attr_id = fields.Many2one('device.device.attributes.value',string="Device Attribute Value")
    _sql_constraints=[
        (
            'unique_name',
            'unique(name)',
            'Choose another value - Name should be unique!'
        )
    ]
