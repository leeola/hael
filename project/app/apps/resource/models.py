# -*- coding: utf-8 -*-
'''
'''

from google.appengine.api import users
from google.appengine.ext import db


class Resource(db.Model):
    
    # Whether or not a resource is listed in queries.
    # Ie, if it's not listed, it's a static page.
    listed = db.BooleanProperty(default=True)
    
    posted_by = db.UserProperty(auto_current_user_add=True)
    posted_on = db.DateTimeProperty(auto_add_now=True)
    
    edited_by = db.UserProperty(auto_current_user=True)
    edited_on = db.DateTimeProperty(auto_now=True)
    
    # The content the client returns.
    source_content = db.TextProperty()
    
    # This will be used in later versions when reST is implemented.
    ## The content that is compiled from source_content.
    #compiled_content = db.TextProperty()
