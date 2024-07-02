from odoo import  fields , models , api
import logging
_logger = logging.getLogger(__name__)


class StudentClasSubject(models.Model):
    _name = 'stu.student_class_subject'
    _description = 'description about student class subject'
    _rec_name = 'subject_id'

    subject_id =fields.Many2one("stu.subject",string="Subject Id")
    class_id =fields.Many2one("stu.class",string="Class Id")
    division_id =fields.Many2one("stu.student_division",string="Division Id")
    max_marks = fields.Integer(string="Max marks")
    ref = fields.Char(string="Study Reference")



    def action_button_method(self):
        print(f"under object action button !")
        try:
            print(f"under try !")
            _logger.info("Your information log message")
            _logger.warning("Your warning log message")
            _logger.error("Your error log message")
        except Exception as e:
            _logger.exception("An error occurred: %s", e)


    def check_orm(self):
        print(f"check orm!")
        # result = self.env['stu.student_class_subject'].search([('max_marks','<=','66'),('max_marks','<=','10')])
        # print(f"data inside stu.student_class_subject obj is {result}")
        # i=1
        # for rec in result:
        #     print(i)
        #     print(f"{rec.subject_id.name} and marks are {rec.max_marks}")
        #     i += 1

        # search_count_result = self.env['stu.student_class_subject'].search_count([('max_marks','<=','66')])
        # print(search_count_result)

        # browse_result = self.env['stu.student_class_subject'].browse(16)
        # print(f"browse result is-------{browse_result}")
        # print(f"subject name is -------{browse_result.ref}")

        # create_var = self.env['stu.student_class_subject'].create({
        #     "max_marks":12,
        #     "ref":"ELon musk"
        # })
        # print(f"record created is ------>{create_var.id}")
        # print(f"record created is ------>{create_var}")
        #
        browse_id = self.env['stu.student_class_subject'].browse(27)
        res=browse_id.write({
            "max_marks":132,
            "ref":"Sanskar SAhu"
        })
        print(f"resutl------->{res}")
        # browse_id = self.env['stu.student_class_subject'].browse(27)
        # result=browse_id.copy()
        # print(f"copied successfully----------{result}")

        # browse_id = self.env['stu.student_class_subject'].browse(28)
        # browse_id.unlink()