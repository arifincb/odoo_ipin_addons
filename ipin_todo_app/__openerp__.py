# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Arifin To-Do Application',
    'description': 'Manage your personal Tasks with this module.',
    'author': 'Arifin',
    'depends': ['mail'],
    'application': True,
    'data': [
        'todo_view.xml',
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
    ],
}
