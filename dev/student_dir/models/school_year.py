from odoo import fields , models ,api
from datetime import  date


class StudentSchoolYear(models.Model):
    _name = "stu.school_year"
    _description = "Description about student school year"


    name = fields.Char(string="name")
    start_date  = fields.Date(string="start_date")
    end_date  = fields.Date(string="end_date")
    isCurrent  = fields.Boolean(string="Is Current ",compute='_compute_is_current',store=True)

    @api.depends('start_date','end_date')
    def _compute_is_current(self):
        today = date.today()
        for records in self:
            if records.start_date and records.end_date:
                records.isCurrent = records.start_date <= today <= records.end_date
            else:
                records.isCurrent = False