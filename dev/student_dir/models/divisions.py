from odoo import  fields , models

class StudentDivision(models.Model):
    _name = 'stu.student_division'
    _description = 'description about student divisions'

    name = fields.Char(string="name",required=True)
    class_id = fields.Many2one("stu.class",string="class_id")
    subjects = fields.One2many("stu.student_class_subject","division_id")
    _sql_constraints = [
        ('field_unique',
         'unique(name)',
         'Choose another value - it has to be unique!')
    ]