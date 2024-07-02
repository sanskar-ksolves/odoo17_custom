from odoo import  fields , models
from datetime import  date,datetime

class StudentClass(models.Model):
    _name = 'stu.student_class'
    _description = 'description about student class'

    name = fields.Char(string="name")
    student_id = fields.Many2one("stu.student_info",string="Student")
    class_id = fields.Many2one("stu.class",string="Class")
    division_id = fields.Many2one("stu.student_division",string="Division")
    year = fields.Many2one("stu.school_year",string="Year")
    subjects = fields.One2many("stu.student_subjects","student_class_id")
