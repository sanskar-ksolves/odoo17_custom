from odoo import  fields , models

class StudentsSubjects(models.Model):
    _name = 'stu.student_subjects'
    _description = 'description about student subjects'

    name = fields.Char(string="name",required=True)
    subject_id = fields.Many2one("stu.subject",string="Subject")
    student_class_id = fields.Many2one("stu.student_class",string="Students Class")
    _sql_constraints = [
        ('field_unique',
         'unique(name)',
         'Choose another value - it has to be unique!')
    ]