from django import forms

class LoginForm(forms.Form):
    email_address = forms.EmailField(label='Email Address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
