from django import forms
from django.forms import DateTimeField


class PlaceholderInput(forms.widgets.Input):
    template_name = 'widgets/placeholder.html'
    input_type = 'text'

    def get_context(self, name, value, attrs):
        context = super(PlaceholderInput, self).get_context(name, value, attrs)
        # context['widget']['attrs']['label'] = "hello"
        # context['widget']['attrs']['maxlength'] = 50
        context['widget']['attrs']['placeholder'] = name.title()
        return context


class HiddenInput(forms.widgets.Input):
    template_name = 'widgets/hiddenholder.html'
    input_type = 'text'

    def get_context(self, name, value, attrs):
        context = super(HiddenInput, self).get_context(name, value, attrs)
        # context['widget']['attrs']['label'] = "hello"
        # context['widget']['attrs']['maxlength'] = 50
        context['widget']['attrs']['placeholder'] = name.title()
        return context


class SelectInput(forms.widgets.Select):
    """
    Add the following 
    <link rel="stylesheet" type="text/css" href="{% static "bower_components/select2/dist/css/select2.min.css" %}">

    <script src="{% static "bower_components/select2/dist/js/select2.full.min.js" %}"></script>
    <script type="application/javascript">

        $('#id_employees').select2();
    </script>
    """
    template_name = 'widgets/selectholder.html'
    input_type = 'text'

    def get_context(self, name, value, attrs):
        context = super(SelectInput, self).get_context(name, value, attrs)
        # context['widget']['attrs']['label'] = "hello"
        # context['widget']['attrs']['maxlength'] = 50
        context['widget']['attrs']['selectholder'] = name.title()
        return context


class MultiSelectInput(forms.widgets.SelectMultiple):
    template_name = 'widgets/multiselectholder.html'
    input_type = 'text'

    def get_context(self, name, value, attrs):
        context = super(MultiSelectInput, self).get_context(name, value, attrs)
        # context['widget']['attrs']['label'] = "hello"
        # context['widget']['attrs']['maxlength'] = 50
        context['widget']['attrs']['selectholder'] = name.title()
        return context


class DateInput(forms.DateInput):
    '''
    Require the following in page
    <script src="{% static "bower_components/bootstrap-datepicker/dist/js/bootstrap-datepicker.min.js" %}"></script>
    <script>
        $('#datepicker').datepicker({
                  autoclose: true, format: 'yyyy-mm-dd',
        }); 
    </script>
    '''
    template_name = 'widgets/dateholder.html'
    input_type = 'text'

    def get_context(self, name, value, attrs):
        context = super(DateInput, self).get_context(name, value, attrs)
        # context['widget']['attrs']['label'] = "hello"
        # context['widget']['attrs']['maxlength'] = 50
        context['widget']['attrs']['selectholder'] = name.title()
        return context

        # class Meta:
        #     css = {'all': ('/static/bower_components/bootstrap-datepicker/dist/css/bootstrap-datepicker.min.css',),}
        #     js = ('/static/bower_components/bootstrap-datepicker/dist/js/bootstrap-datepicker.js',)


class DateTimeInput(forms.DateTimeInput):
    '''
    Require the following in page
    <script src="{% static "bower_components/bootstrap-datepicker/dist/js/bootstrap-datepicker.min.js" %}"></script>
    <script>
        $('#datepicker').datepicker({
                  autoclose: true, format: 'mm/dd/yyyy',
        }); 
    </script>
    '''

    template_name = 'widgets/datetimeholder.html'
    input_type = 'text'

    def get_context(self, name, value, attrs):
        context = super(DateTimeInput, self).get_context(name, value, attrs)
        # context['widget']['attrs']['label'] = "hello"
        # context['widget']['attrs']['maxlength'] = 50
        context['widget']['attrs']['selectholder'] = name.title()
        return context

        # class Meta:
        #     css = {'all': ('/static/bower_components/bootstrap-datetimepicker/css/bootstrap-datetimepicker.css',),}
        #     js = ('/static/bower_components/bootstrap-datetimepicker/js/bootstrap-datetimepicker.js',)


class TimeInput(forms.TimeInput):
    '''
    Require the following in page
    <script src="{% static "bower_components/bootstrap-datepicker/dist/js/bootstrap-datepicker.min.js" %}"></script>
    <script>
        $('#datepicker').datepicker({
                  autoclose: true
        }); 
    </script>
    '''
    template_name = 'widgets/timeholder.html'
    input_type = 'text'

    def get_context(self, name, value, attrs):
        context = super(TimeInput, self).get_context(name, value, attrs)
        # context['widget']['attrs']['label'] = "hello"
        # context['widget']['attrs']['maxlength'] = 50
        context['widget']['attrs']['selectholder'] = name.title()
        return context

        # class Media:
        #     css = {'all': ('/static/plugins/timepicker/bootstrap-timepicker.min.css',),}
        #     js = ('/static/plugins/timepicker/bootstrap-timepicker.min.js',)


class MyDateTimeField(DateTimeField):
    def __init__(self, input_formats=None, *args, **kwargs):
        self.widget = DateTimeInput(attrs={'label': kwargs.pop('label'), 'labelicon': 'fa', 'id': kwargs.pop('id')})
        super(MyDateTimeField, self).__init__(input_formats, *args, **kwargs)
        self.label = ''


class MyDateField(DateTimeField):
    def __init__(self, input_formats=None, *args, **kwargs):
        self.widget = DateInput(attrs={'label': kwargs.pop('label'), 'labelicon': 'fa', 'id': kwargs.pop('id')})
        super(MyDateField, self).__init__(input_formats, *args, **kwargs)
        self.label = ''


class MyDateRangeField(DateTimeField):
    def __init__(self, input_formats=None, *args, **kwargs):
        self.widget = DateInput(attrs={'label': kwargs.pop('label'), 'labelicon': 'fa', 'id': kwargs.pop('id')})
        super(MyDateRangeField, self).__init__(input_formats, *args, **kwargs)
        self.label = ''


class MyDateTimeRangeField(DateTimeField):
    def __init__(self, input_formats=None, *args, **kwargs):
        self.widget = DateInput(attrs={'label': kwargs.pop('label'), 'labelicon': 'fa', 'id': kwargs.pop('id')})
        super(MyDateTimeRangeField, self).__init__(input_formats, *args, **kwargs)
        self.label = ''


class MyTimeField(DateTimeField):
    def __init__(self, input_formats=None, *args, **kwargs):
        self.widget = TimeInput(attrs={'label': kwargs.pop('label'), 'labelicon': 'fa', 'id': kwargs.pop('id')})
        super(MyTimeField, self).__init__(input_formats, *args, **kwargs)
        self.label = ''


class MyTextInput(forms.TextInput):
    def __init__(self, attrs=None):
        self.attrs = attrs
        super(MyTextInput, self).__init__(attrs)


class MyCharField(forms.CharField):
    def __init__(self, max_length=None, min_length=None, strip=True, empty_value='', *args, **kwargs):
        self.widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': kwargs.pop('placeholder')})
        super(MyCharField, self).__init__(max_length, min_length, strip, empty_value, *args, **kwargs)


class MyPasswordField(forms.CharField):
    def __init__(self, max_length=None, min_length=None, strip=True, empty_value='', *args, **kwargs):
        self.widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': kwargs.pop('placeholder')})
        super(MyPasswordField, self).__init__(max_length, min_length, strip, empty_value, *args, **kwargs)


class MyMultipleChoiceField(forms.MultipleChoiceField):
    def __init__(self, choices=(), required=True, widget=None, label=None, initial=None, help_text='', *args, **kwargs):
        self.widget = forms.SelectMultiple(attrs={'class': 'form-control'})
        super(MyMultipleChoiceField, self).__init__(choices, required, widget, label, initial, help_text, *args,
                                                    **kwargs)


class MyDateRangeButtonField(forms.MultipleChoiceField):
    def __init__(self, choices=(), required=True, widget=None, label=None, initial=None, help_text='', *args, **kwargs):
        self.widget = forms.SelectMultiple(attrs={'class': 'form-control'})
        super(MyDateRangeButtonField, self).__init__(choices, required, widget, label, initial, help_text, *args,
                                                     **kwargs)


class MyMultipleCheckboxField(forms.MultipleChoiceField):
    def __init__(self, choices=(), required=True, widget=None, label=None, initial=None, help_text='', *args, **kwargs):
        self.widget = forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'})
        super(MyMultipleCheckboxField, self).__init__(choices, required, widget, label, initial, help_text, *args,
                                                      **kwargs)


class MyChoiceSelectField(forms.ChoiceField):
    def __init__(self, choices=(), required=True, widget=None, label=None, initial=None, help_text='', *args, **kwargs):
        self.widget = forms.Select(attrs={'class': 'form-control'})
        super(MyChoiceSelectField, self).__init__(choices, required, widget, label, initial, help_text, *args, **kwargs)


class MyChoiceRadioField(forms.ChoiceField):
    def __init__(self, choices=(), required=True, widget=None, label=None, initial=None, help_text='', *args, **kwargs):
        self.widget = forms.RadioSelect()
        super(MyChoiceRadioField, self).__init__(choices, required, widget, label, initial, help_text, *args, **kwargs)


# forms.MultipleChoiceField(widget=MultiSelectInput(attrs={'data-placeholder': "Select skills"}), label="Skills",choices=CHOICES)
class MyMultipleChipField(forms.MultipleChoiceField):
    def __init__(self, choices=(), required=True, widget=None, label=None, initial=None, help_text='', *args, **kwargs):
        self.widget = MultiSelectInput(attrs={'data-placeholder': kwargs.pop('placeholder')})
        super(MyMultipleChipField, self).__init__(choices, required, widget, label, initial, help_text, *args, **kwargs)