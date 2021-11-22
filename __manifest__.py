# -*- coding: utf-8 -*-
{
    'name': "Paint image region",

    'summary': """
        Paint image region 
        """,

    'description': """
        Test module for area painting in Product-Category
    """,

    'author': "rosales9146@gmail.com",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],
    #TODO other depends
    #pip3 install numpy
    #pip3 install opencv-python

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_category_views.xml',
        'views/product_template_views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
