from django import forms
from .models import Userform

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model = Userform
        fields = ['username','name', 'dob', 'gender', 'phone_number', 'email', 'address', 'district', 'branch', 'account_type']
