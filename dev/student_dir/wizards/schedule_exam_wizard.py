from odoo import fields, models, api


class ExamSchedulerWizard(models.TransientModel):
    _name = 'stu.schedule.exam'
    _description = 'Wizard to schedule exams for students in a class'

    class_id = fields.Many2one('stu.class', string="Class", required=True)

    class_subject = fields.Many2one("stu.student_class_subject",string="classSub")

    exam_date = fields.Date(string="Exam Date", required=True)

    def schedule_exams(self):
        print(f"Students ------{self.class_id.student_ids}")
        students = self.class_id.student_ids
        subjects = self.env['stu.subject'].search([('class_id', '=', self.class_id.id)])
        print(f"subjects are-----{subjects}")
        print(f"self.class_id are-----{self.class_id}")

        for subject in subjects:
            self.env['stu.exams'].create({
                'name': f'{subject.name}-{self.exam_date}',
                'subject_id': subject.id,
                'class_id': self.class_id.id,
                'student_ids': students,
                'exam_date': self.exam_date,
                'exam_completed': False,
            })
        print(f"exam scheduled..")
