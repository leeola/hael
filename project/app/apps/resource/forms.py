# -*- coding: utf-8 -*-
'''
'''

from tipfy.ext.genshi import render_response
from tipfy.ext.wtforms import Form, BooleanField, validators
from fields import TextField


class ResourceForm(Form):
    title = TextField('Title', autofocus=True, placeholder='The Post Title')
    body = TextField('Body', [validators.Required()], required=True)
    
    listed = BooleanField('Is this resource listed?')
    
    template = TextField('Template', [validators.Required()], default='page.html')
