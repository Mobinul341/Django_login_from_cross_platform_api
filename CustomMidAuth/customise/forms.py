from django import forms
from . models import FormModel

class FormModelForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput())
    


