from odoo import fields, models, api

class StudentInfoWizard(models.TransientModel):
    _name = 'stu.student_info_wizard'
    _description = 'Wizard to manage student information'

    student_id = fields.Many2one('stu.student_info', string="Student", readonly=True)
    name = fields.Char(string="Name", required=True)
    roll_no = fields.Integer(string="Roll No", required=True)
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age", compute='_compute_age_with_DOB', store=True)
    address = fields.Char(string="Address")
    class_id = fields.Many2one("stu.class", string="Class")
    subject_ids = fields.Many2many("stu.subject", string="Subjects")
    fees_id = fields.One2many("stu.odoo_fees", 'student_id', string="Fees")

    @api.depends('dob')
    def _compute_age_with_DOB(self):
        for record in self:
            if record.dob:
                birth_date = fields.Date.from_string(record.dob)
                today = fields.Date.today()
                record.age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            else:
                record.age = 0

    @api.model
    def default_get(self, fields):
        res = super(StudentInfoWizard, self).default_get(fields)
        student_id = self.env.context.get('active_id')
        if student_id:
            student = self.env['stu.student_info'].browse(student_id)
            res.update({
                'student_id': student.id,
                'name': student.name,
                'roll_no': student.roll_no,
                'dob': student.dob,
                'address': student.address,
                'class_id': student.class_id.id,
                    'subject_ids': [(6, 0, student.subject_ids.ids)],
                # 'fees_id': [(0, 0, {'amount': fee.amount, 'date': fee.date_paid}) for fee in student.fees_id],
            })
        return res

    def action_save_student_info(self):
        if self.student_id:
            # Update existing student
            self.student_id.write({
                'name': self.name,
                'roll_no': self.roll_no,
                'dob': self.dob,
                'address': self.address,
                'class_id': self.class_id.id,
                'subject_ids': [(6, 0, self.subject_ids.ids)],
                # 'fees_id': [(0, 0, {'amount': fee.amount, 'date': fee.date_paid}) for fee in self.fees_id],
            })
        else:
            # Create new student
            self.env['stu.student_info'].create({
                'name': self.name,
                'roll_no': self.roll_no,
                'dob': self.dob,
                'address': self.address,
                'class_id': self.class_id.id,
                'subject_ids': [(6, 0, self.subject_ids.ids)],
                # 'fees_id': [(0, 0, {'amount': fee.amount, 'date': fee.date_paid}) for fee in self.fees_id],
            })
        return {'type': 'ir.actions.act_window_close'}
