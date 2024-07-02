from odoo import  fields,api,models

class teacher_hr(models.Model):
    _name = "hr.teacher"
    _description = """
                    This is the description about teacher which is kind of HR , and is associated with class as teacher has many classes
    """

    name = fields.Char(string="Name")
    age  = fields.Integer(string="Age")
    color = fields.Integer(string='Color')
    class_id = fields.Many2many("stu.class","class_teacher_rel","teacher_id","class_id",string="Class")