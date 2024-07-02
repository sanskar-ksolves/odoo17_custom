from odoo import  fields , models,api,_
from datetime import  date,datetime
from odoo.exceptions import  ValidationError


class TestWizard(models.TransientModel):
    _name="test.wizard"
    _description = "Description of test wizard"

    name = fields.Char(string="name")
    roll_no = fields.Integer(string="roll no",required=True)
    dob = fields.Date(string="DOB")
    age = fields.Integer(string="age",compute='_compute_age_with_DOB',store=True)
    address = fields.Char(string="address")
    test = fields.Integer(string="test",compute='_compute_test_field',store=True)

    class_id = fields.Many2one("stu.class",string="Class")
    subject_ids = fields.Many2many("stu.subject",string="Subjects")
    fees_id  = fields.One2many("stu.odoo_fees",'student_id',string="Fees")


    # parent_name
    # student_history
    _sql_constraints = [
        ('field_unique',
        'unique(roll_no)',
        'Roll No. should be unique Choose another value!')
    ]


    @api.depends('dob')
    def _compute_age_with_DOB(self):
        for record in self:
            if record.dob:
                birth_date = fields.Date.from_string(record.dob)
                today = date.today()
                record.age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            else:
                record.age = 0
    @api.constrains('age')
    def val_age(self):
        for record in self:
            if record.age <= 18:
                raise ValidationError (_('The age must be above then 18'))

    @api.model
    def test_cron_job_action(self):
        print(f"testing of corn job!")

    # @api.depends('test')
    def _compute_test_field(self):
        for record in self:
            record.test += 1
    def update_record_button(self):
        print(f"wizard test")