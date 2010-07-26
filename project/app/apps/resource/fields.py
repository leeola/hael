# -*- coding: utf-8 -*-
'''A slew of HTML5 focused Fields.
'''


from tipfy.ext.wtforms import Field
from tipfy.ext.wtforms.widgets import Input


class HTML5Input(Input):
    '''The base for the new HTML5 Inputs.
    
    A quick explanation for this is that HTML5 offers some new attributes
    that are not available by the default wtforms. Normally, any additional
    parameters given to the input constructor are passed as input attributes,
    with the exception (to my knowledge) of the new style attributes like
    "required", and "autofocus", etc.'''

    def __init__(self):
        ''''''
        super(HTML5Input, self).__init__(**kwargs)


class TextInput(HTML5Input):
    ''''''

    def __init__(self, autofocus=False, placeholder=None, required=False,
                 **kwargs):
        ''''''
        super(HTML5Input, self).__init__(**kwargs)
        
        self.autofocus = autofocus
        self.placeholder = placeholder
        self.required = required


class HTML5Field(Field):
    '''A field that provides some generic new field attributes found in HTML5.
    '''
    widget = HTML5Input()
    
    def __init__(self, label='', validators=None, **kwargs):
        super(HTML5Field, self).__init__(label, validators, **kwargs)


class TextField(HTML5Field):
    '''
    '''
    widget = TextInput(input_type='text')
    
    def __init__(self, label='', validators=None, autofocus=False,
                 placeholder=None, required=False, **kwargs):
        super(TextField, self).__init__(label, validators, **kwargs)
        
        self.widget.autofocus = autofocus
        self.widget.placeholder = placeholder
        self.widget.required = required


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
    
    def __init__(self, label='', validators=None, remove_duplicates=True, **kwargs):
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
