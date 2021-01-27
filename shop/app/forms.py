from django import forms
from django.forms import PasswordInput

ENG = (('A1', 'A1'),('B1', 'B1'),('B2', 'B2'))
GENDER = (('m', 'male'), ('f', 'female'))

class EnglishForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30, required=True)
    age = forms.IntegerField(label='Age', min_value=0, required=True)
    pol = forms.ChoiceField(choices=GENDER, required=True)
    level = forms.ChoiceField(choices=ENG, required=True)

class LoginForm(forms.Form):
    name = forms.CharField(label='username', max_length=30, required=True)
    password = forms.CharField(label='password', widget=PasswordInput, max_length=30, required=True)

class LogoutForm(forms.Form):
    pass

class SearchForm(forms.Form):
    field = forms.CharField(label='search', max_length=30, required=True)

class RegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=30, required=True)
    password = forms.CharField(label='password', max_length=30, required=True)
    confirm = forms.CharField(label='confirm', max_length=30, required=True)
