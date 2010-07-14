# -*- coding: utf-8 -*-
'''
'''

from tipfy import Rule


def get_rules(app):
    rules = [
        # Request all resources.
        Rule('/', endpoint='resources', handler='apps.new.handlers.ResourcesHandler'),
        
        # Request a specific resource
        Rule('/<resource_name>', endpoint='resource', handler='apps.new.handlers.ResourceHandler'),
    ]

    return rules
