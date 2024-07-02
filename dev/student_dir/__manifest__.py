{
    'name': 'Student Management',
    'version': '17.0.0.0',
    'summary': 'summary of  Student managemnt',
    'sequence': 10,
    'author': "Ksolves",
    'description': """
description about Student management
""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizards/test_wizard.xml',
        'wizards/schedule_exam_wizard.xml',
        'wizards/student_info_wizard_view.xml',
        # 'views/actions.xml',
        'views/menus.xml',
        'views/class_subject.xml',
        'views/divisions.xml',
        'views/exam.xml',
        'views/menus.xml',
        'views/school_year.xml',
        'views/stu_class.xml',
        'views/student.xml',
        'views/student_class.xml',
        'views/student_exam.xml',
        'views/student_subjects.xml',
        'views/subjects.xml',
        'views/fees.xml',
        'views/teacher_hr.xml',
        'reports/report.xml',
        'views/test_cron.xml',
        'reports/class_report.xml',
        # 'views/custom_action_template.xml',
        # 'views/client_action.xml',

    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'student_dir/static/src/js/custom_action.js',
    #     ],
    # },

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
