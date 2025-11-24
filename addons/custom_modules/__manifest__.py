{
    'name': 'My Debug Module',
    'version': '1.0',
    'summary': 'A simple module for debugging in Odoo',
    'description': 'This module provides a basic model to test debugging.',
    'author': 'Your Name',
    'depends': ['base'],  # Phụ thuộc vào module base
    'data': [
        'views/debug_test_views.xml',
    ],
    'installable': True,
    'application': False,
}