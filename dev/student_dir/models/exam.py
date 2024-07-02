from odoo import  fields , models , api

class StudentExam(models.Model):
    _name = 'stu.exams'
    _description = 'description about student exam'

    name = fields.Char(string="name",required=True)
    class_id = fields.Many2one("stu.class",string="Class")
    class_subject = fields.Many2one("stu.student_class_subject",string="classSub")
    ref = fields.Char(string="Study Reference")
    exam_date = fields.Date(string="Exam Date")
    exam_completed = fields.Boolean(string="Exam Complete Status")
    student_ids = fields.Many2many('stu.student_info','student_exam_rel','exam_id','student_id', string="Student")
    subject_id = fields.Many2one('stu.subject', string="Subject")
    marks = fields.Integer(string="Marks")
    _sql_constraints = [
        ('field_unique',
         'unique(name)',
         'Choose another value - it has to be unique!')
    ]

    @api.onchange('class_subject')
    def onchange_class_subject(self):
        self.ref = self.class_subject.ref

    @api.onchange('class_id')
    def _onchange_class_id(self):
        if self.class_id:
            self.student_ids = [(6, 0, self.class_id.student_ids.ids)]
        else:
            self.student_ids = [(6, 0, [])]


class TestInheritModel(models.Model):
    _inherit = "stu.student_class_subject"

    new_field = fields.Char(string="New Field")
