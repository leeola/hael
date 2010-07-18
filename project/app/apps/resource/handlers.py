# -*- coding: utf-8 -*-
'''
'''

from forms import ResourceForm

from tipfy import (RequestHandler, Response, cached_property,
                   NotImplemented, NotFound)
from tipfy.ext.genshi import render_response


class ResourceHandler(RequestHandler):
    '''The handler for a single resource request.
    '''
    
    @cached_property
    def form(self):
        return ResourceForm(self.request)
    
    def delete(self):
        '''Delete this resource.'''
        return NotImplemented()
    
    def get(self, **kwargs):
        '''Show this resource if it exists.
        If not, display a creation form.'''
        
        context = {'form':self.form}
        
        return render_response('edit_resource.html', context)
    
    def post(self, **kwargs):
        '''Modify this resource.'''
        
        if self.form.validate():
            # Do stuff
            return NotImplemented()
        else:
            return self.get(**kwargs)
    
    def put(self, **kwargs):
        '''Update/Create this resource.'''
        return NotImplemented()
        
        if self.form.validate():
            # Do stuff
            return NotImplemented()
        else:
            return self.get(**kwargs)


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
