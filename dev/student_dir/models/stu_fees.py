from odoo import  fields,api,models

class StudentFees(models.Model):
    _name = "stu.odoo_fees"
    _description = """
                    Desciption about student's institution fees.
                   """

    name = fields.Char(string="Monthly Fees")
    paid_current_month = fields.Boolean(string="Is fees paid",default=False)
    current_month_fees = fields.Integer(string="Fees Amount")
    amount = fields.Float(string="Amount",required=True)
    date_paid = fields.Date(string="Date Paid",required=True)
    student_id = fields.Many2one("stu.student_info",string="Student",required=True)
