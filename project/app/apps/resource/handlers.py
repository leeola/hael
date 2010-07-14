# -*- coding: utf-8 -*-
'''
'''

from tipfy import RequestHandler, Response, NotImplemented, NotFound
from tipfy.ext.genshi import render_response


class ResourceHandler(RequestHandler):
    '''The handler for a single resource request.
    '''
    
    def delete(self):
        '''Delete this resource.'''
        return NotImplemented()
    
    def get(self):
        '''Show this resource.'''
        return NotImplemented()
    
    def post(self):
        '''Modify this resource.'''
        return NotImplemented()
    
    def put(self):
        '''Update/Create this resource.'''
        return NotImplemented()


class ResourcesHandler(RequestHandler):
    
    def delete(self):
        '''A resouce listing cannot be deleted.'''
        return NotFound()
    
    def get(self):
        '''Show any resources matching criteria.'''
        return NotImplemented()
    
    def post(self):
        '''The client wants to create a resource but leave the URI up to the
        server.'''
        return NotImplemented()
    
    def put(self):
        '''A resource listing cannot have information put into it.'''
        return NotFound()
