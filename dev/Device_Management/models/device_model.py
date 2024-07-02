from odoo import  fields,models,api

class DeviceModel(models.Model):
    _name = "device.device.model"
    _description = """
                    Device assignment details 
                   """
    name = fields.Char(string="Name", required=True)
    device_type_id = fields.Many2one('device.device.type',string="Device Type")
    device_brand_id = fields.Many2one('device.device.brand',string="Device Brand")

    _sql_constraints=[
        (
            'unique_name',
            'unique(name)',
            'Choose another value - Name should be unique!'
        )
    ]
