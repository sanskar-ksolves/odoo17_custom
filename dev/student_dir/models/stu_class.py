from odoo import  fields,models

class StudentClass(models.Model):
    _name = "stu.class"
    _description = "Description about student class"

    name = fields.Char(string="name")
    code = fields.Char(string="code", required=True)
    student_ids = fields.One2many("stu.student_info","class_id",string="Students")
    subject_id = fields.Many2many("stu.subject","student_class_subject_new_rel","stu_new_class_id","stu_new_subject_id")
    teacher_ids = fields.Many2many("hr.teacher", "class_teacher_rel", "class_id", "teacher_id", string="Teachers")



    _sql_constraints = [
        ('field_unique',
         'unique(code)',
         'Choose another value - it has to be unique!')
    ]