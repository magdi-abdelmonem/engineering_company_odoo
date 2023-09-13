# -*- coding: utf-8 -*-
{
    'name': "Engineering ",

    'summary': "Engineering company",

    'description': "This is the Engineering company system that organize the work ",

    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','website'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        'views/projects_views.xml',
        'views/engineers_views.xml',
        'views/project_manager.xml',
        'views/projects_template.xml',
        'wizard/cancel_project_wizard.xml',
        'wizard/add_engineer_to_project.xml',
        'reports/engineers_report.xml',
        'reports/projects_report.xml',
        'data/eng_sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
