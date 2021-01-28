from django import forms
from django.core.exceptions import ValidationError
from django.forms import PasswordInput

ENG = (('A1', 'A1'), ('B1', 'B1'), ('B2', 'B2'))
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
    password = forms.CharField(label='password', max_length=30, required=True, widget=PasswordInput)
    confirm = forms.CharField(label='confirm', max_length=30, required=True, widget=PasswordInput)

    def clean_confirm(self):
        user_pass = self.cleaned_data.get('password')
        conf = self.cleaned_data.get('confirm')
        if conf != user_pass:
            raise forms.ValidationError("Passwords are different")
        return conf

class CommentForm(forms.Form):
    msg = forms.CharField(label='comment', max_length=100, required=True, widget=forms.Textarea)

class ChangePassword(forms.Form):
    old = forms.CharField(label='old password', max_length=30, required=True, widget=PasswordInput)
    new = forms.CharField(label='new password', max_length=30, required=True, widget=PasswordInput)
    newconf = forms.CharField(label='confirm new', max_length=30, required=True, widget=PasswordInput)

    def clean_newconf(self):
        password = self.cleaned_data.get('new')
        password_confirm = self.cleaned_data.get('newconf')
        if password != password_confirm:
            raise forms.ValidationError("Passwords are different")
        return password_confirm
