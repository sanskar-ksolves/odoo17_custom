from odoo import fields , models

class Subjects(models.Model):
    _name = "stu.subject"
    _description = "Description about student subject"
    _rec_name = "name"

    name = fields.Char(string="name")
    code = fields.Char(string="code",required=True)
    class_id = fields.Many2one("stu.class",String="Class")
    student_id = fields.Many2many("stu.student_info","student_subject_rel","stu_class_id","stu_student_id",String="Studnet")

    color = fields.Integer(string='Color')

    _sql_constraints = [
        ('field_unique',
        'unique(name)',
        'Choose another value - it should be unique')
    ]