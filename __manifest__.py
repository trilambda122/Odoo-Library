# -*- coding: utf-8 -*-
{
    'name': "Libaray APP",

    'summary': """
        A Cool Learning App""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://sschilling.com",
    'license' : 'AGPL-3'

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'category' : 'Services/Library'

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/book_view.xml',
        'views/library_menu',
        'views/book_list_template',
        ],
    'application':True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
