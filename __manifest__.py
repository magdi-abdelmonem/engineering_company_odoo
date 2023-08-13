# -*- coding: utf-8 -*-
{
    'name': "Engineering ",

    'summary': "Engineering company",

    'description': "This is the Engineering company system that organize the work ",

    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        'views/engineers_views.xml',
        'views/projects_views.xml',
        'wizard/wizard.xml',
        'reports/engineers_report.xml',
        'reports/projects_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
