from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(max_length=100)
    Phone_no = forms.CharField(max_length=10)
    Email = forms.EmailField()
    Password = forms.CharField(max_length=8)
    ConForm_Password = forms.CharField(max_length=8)

class LoginForm(forms.Form):
    Email = forms.EmailField()
    Password = forms.CharField(max_length=8)