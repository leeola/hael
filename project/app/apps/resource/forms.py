# -*- coding: utf-8 -*-
'''
'''

from tipfy.ext.genshi import render_response
from tipfy.ext.wtforms import Form, BooleanField, TextField, validators

class ResourceForm(Form):
    title = TextField('Title')
    body = TextField('Body', [validators.Required()])
    
    listed = BooleanField('Is this resource listed?')
    
    template = TextField('Template', [validators.Required()], default='page.html')
