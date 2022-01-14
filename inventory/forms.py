import re

from django import forms
from django.contrib.auth.models import User

from .models import UsersDetails, Product, OrderSupply, Order
from .mywidgets import PlaceholderInput, SelectInput


class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class AddUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)

    # assign_device = ModelMultipleChoiceField(queryset=DeviceList.objects.all(), widget=Select2MultipleWidget)

    email = forms.EmailField(min_length=3, label='', required=True, widget=PlaceholderInput(
        attrs={'maxlength': 100, 'label': 'Email', 'helptext': 'Input the email.',
               'labelicon': 'fa'}))

    password = forms.CharField(min_length=3, label='', required=True, widget=PlaceholderInput(
        attrs={'maxlength': 100, 'label': 'Password', 'helptext': 'Input the password.',
               'labelicon': 'fa', 'type': 'password'}))

    confirm_password = forms.CharField(min_length=3, label='', required=True, widget=PlaceholderInput(
        attrs={'maxlength': 100, 'label': 'Confirm Password', 'helptext': 'Input the password again.',
               'labelicon': 'fa', 'type': 'password'}))

    class Meta:
        model = UsersDetails
        fields = ['type', 'name', 'current_address', 'mobile', 'status', 'email']
        widgets = {
            'type': SelectInput(
                attrs={'maxlength': 10, 'label': 'department', 'helptext': 'Select the Type.',
                       'labelicon': 'fa'}
            ),
            'name': PlaceholderInput(
                attrs={'maxlength': 10, 'label': 'Name', 'helptext': 'Input the Name.',
                       'labelicon': 'fa'}),
            'current_address': PlaceholderInput(
                attrs={'maxlength': 10, 'label': 'Address', 'helptext': 'Input the Address.',
                       'labelicon': 'fa'}),

            'status': SelectInput(
                attrs={'maxlength': 10, 'label': 'department', 'helptext': 'Input the Status.',
                       'labelicon': 'fa'}
            ),
            'mobile': PlaceholderInput(
                attrs={'maxlength': 10, 'label': 'Mobile', 'helptext': 'Input the mobile.',
                       'labelicon': 'fa'}
            ),

        }
        labels = {
            'name': '', 'current_address': '', 'status': 'Status', 'mobile': ''
        }

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        phno_pattern = re.compile(r'^[0-9]{10}$')

        if not phno_pattern.match(self.cleaned_data['mobile']):
            raise forms.ValidationError(message='Not a valid phone number')

        if password == confirm_password:
            try:
                new_user = User.objects.create_user(username=self.cleaned_data.get('email'),
                                                    email=self.cleaned_data.get('email'),
                                                    password=self.cleaned_data.get('password'),
                                                    first_name=self.cleaned_data.get('name'))
                new_user.save()
            except Exception as e:
                raise forms.ValidationError("User already exists!!")
            return super(AddUserForm, self).clean()
        else:
            raise forms.ValidationError('Sorry, password entered is not matching')

    def save(self, commit=True):
        user = User.objects.filter(username=self.data.get('email')).first()
        print('befo ')
        if user is None:
            print('after')
            # create new user
            new_user = User.objects.create_user(username=self.data.get('email'),
                                                email=self.data.get('email'),
                                                password=self.data.get('password'),
                                                first_name=self.cleaned_data.get('name'))
            emp = UsersDetails()
            emp.name = self.cleaned_data.get('name')
            emp.current_address = self.cleaned_data.get('current_address')
            emp.mobile = self.cleaned_data.get('mobile')
            emp.email = self.cleaned_data.get('email')
            print('emp mail', self.cleaned_data.get('email'))
            emp.status = self.cleaned_data.get('status')
            emp.save()
            new_user.save()
        instance = super(AddUserForm, self).save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance


class EditUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(min_length=3, label='', required=True, widget=PlaceholderInput(
        attrs={'maxlength': 100, 'label': 'Email', 'helptext': 'Input the email.',
               'labelicon': 'fa'}))

    class Meta:
        model = UsersDetails
        fields = ['name', 'current_address', 'mobile', 'status']
        widgets = {
            'name': PlaceholderInput(
                attrs={'maxlength': 10, 'label': 'Employee name', 'helptext': 'Input the Employee name.',
                       'labelicon': 'fa'}),
            'current_address': PlaceholderInput(
                attrs={'maxlength': 10, 'label': 'Employee ID', 'helptext': 'Input the Employee ID.',
                       'labelicon': 'fa'}),

            'mobile': PlaceholderInput(
                attrs={'maxlength': 10, 'label': 'Mobile', 'helptext': 'Input the mobile.',
                       'labelicon': 'fa'}
            ),
            'status': SelectInput(
                attrs={'maxlength': 10, 'label': 'Company', 'helptext': 'Input the Company.',
                       'labelicon': 'fa'}
            ),

        }
        labels = {
            'name': '', 'current_address': '', 'mobile': '', 'status': 'status',
        }

    def save(self, commit=True):
        instance = super(EditUserForm, self).save(commit=False)

        if commit:
            instance.save()
        instance.user.email = self.cleaned_data['email']
        instance.user.username = self.cleaned_data['email']
        instance.user.first_name = self.cleaned_data['name']
        instance.user.save()
        return instance


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'subcategory', 'productbrand', 'productmodel', 'productname', 'productunit', 'pricebuy',
                  'pricesell')


class OrderSupplyForm(forms.ModelForm):
    class Meta:
        model = OrderSupply
        fields = ('supplier', 'product', 'qty', 'arrivedat', 'arrived')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

