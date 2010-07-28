# -*- coding: utf-8 -*-
'''A slew of HTML5 focused Fields.
'''


from cgi import escape

import wtforms
from tipfy.ext.wtforms import Field
from wtforms.widgets import Input, HTMLString


def html_params(*args, **kwargs):
    '''
    Generate HTML parameters from inputted keyword arguments, with the added
    ability to handle non-keyword parameters, such as the new HTML5
    parameters.

    >>> html_params('autofocus', name='text1', id='f',class_='text')
    u'class="text" id="f" name="text1" autofocus'
    '''
    params = []
    for k,v in sorted(kwargs.iteritems()):
        if k in ('class_', 'class__', 'for_'):
            k = k[:-1]
        params.append(u'%s="%s"' % (unicode(k), escape(unicode(v), quote=True)))
    params.extend(sorted(args))
    return u' '.join(params)


class HTML5Input(Input):
    '''The base for the new HTML5 Inputs.
    
    A quick explanation for this is that HTML5 offers some new attributes
    that are not available by the default wtforms. Normally, any additional
    parameters given to the input constructor are passed as input attributes,
    with the exception (to my knowledge) of the new style attributes like
    "required", and "autofocus", etc.'''
    
    def __call__(self, field, *args, **kwargs):
        '''
        '''
        
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()
        return HTMLString(u'<input %s />' % html_params(name=field.name,
                                                        *args,
                                                        **kwargs))


class TextInput(HTML5Input):
    ''''''
    pass


class HTML5Field(Field):
    '''A field that provides some generic new field attributes found in HTML5.
    '''
    widget = HTML5Input()
    
    def __init__(self, label='', validators=None, **kwargs):
        super(HTML5Field, self).__init__(label, validators, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.widget(self, *args, **kwargs)

class TextField(HTML5Field, wtforms.TextField):
    '''
    '''
    widget = TextInput(input_type='text')
    
    def __init__(self, label='', validators=None, autofocus=False,
                 placeholder=None, required=False, **kwargs):
        super(TextField, self).__init__(label, validators, **kwargs)
        
        self.autofocus = autofocus
        self.placeholder = placeholder
        self.required = required

    def __call__(self, *args, **kwargs):
        args = [l for l in args]
        if self.autofocus:
            args.append('autofocus')
        if self.placeholder is not None:
            kwargs['placeholder'] = self.placeholder
        if self.required:
            args.append('required')
        args = tuple(args)
        return self.widget(self, *args, **kwargs)

class EmailField(TextField):
    '''
    '''
    widget = TextInput(input_type='email')
    
    def __init__(self, label='', validators=None, **kwargs):
        super(HTML5Field, self).__init__(label, validators, **kwargs)


class PhoneField(TextField):
    '''
    '''
    widget = TextInput(input_type='tel')
    
    def __init__(self, label='', validators=None, **kwargs):
        super(HTML5Field, self).__init__(label, validators, **kwargs)


class TagListField(TextField):
    widget = TextInput()
    
    def __init__(self, label='', validators=None, remove_duplicates=True,
                 **kwargs):
        super(TagListField, self).__init__(label, validators, **kwargs)
        self.remove_duplicates = remove_duplicates

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []
        
        if self.remove_duplicates:
            self.data = list(self._remove_duplicates(self.data))

    @classmethod
    def _remove_duplicates(cls, seq):
        '''Remove duplicates in a case insensitive,
        but case preserving manner'''
        d = {}
        for item in seq:
            if item.lower() not in d:
                d[item.lower()] = True
                yield item
