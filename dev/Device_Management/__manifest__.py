{
    'name': 'Device Management',
    'version': '17.0.0.0',
    'summary': 'This module shows how to manage an device with proper guidance and support',
    'sequence': 10,
    'author': "Ksolves",
    'description': """
This module includes the descirption of management and guidance about how to manage an device .
""",
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/menus.xml',
        'views/device_type.xml',
        'views/device.xml',
        'views/device_attr.xml',
        'views/device_assignment.xml',
        'views/device_attr_assignment.xml',
        'views/device_attr_value.xml',
        'views/device_brand.xml',
        'views/device_model.xml',
        'views/employee.xml',

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
