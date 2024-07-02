from odoo import  fields , models
from datetime import  date,datetime

class StudentExam(models.Model):
    _name = 'stu.student_exam'
    _description = 'description about student exam'

    name = fields.Char(string="name")
    exam_id = fields.Many2one("stu.student_class_subject",string="Class Subject")
    student_class_id = fields.Many2one("stu.student_class",string="Student Class")
    marks = fields.Integer(string="marks")
