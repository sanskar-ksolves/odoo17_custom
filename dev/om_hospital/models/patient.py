from odoo import  api,models,fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = "Patients Records updated"

    name = fields.Char(strng='name',required=True)
    age  = fields.Integer(string='age')
    is_child = fields.Boolean(string='Is child ?')
    notes = fields.Text(string="Text")
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string='Gender')