from django import forms

class SignUpForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30, required=True)
    last_name = forms.CharField(label='Last Name', max_length=30, required=True)
    phone_number = forms.CharField(label='Phone Number', max_length=10, required=True)
    email_address = forms.EmailField(label='Email Address', max_length=254, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
