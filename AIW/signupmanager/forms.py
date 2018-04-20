from django import forms

class SignUpForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    phone_number = forms.CharField(label='Phone Number', max_length=10)
    email_address = forms.EmailField(label='Email Address', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    location_list = [('Bangalore', 'Bangalore'), ('Chennai','Chennai'), ('Delhi', 'Delhi'), ('Hyderabad', 'Hyderabad'), ('Mumbai', 'Mumbai'), ('Pune', 'Pune')]
    location = forms.ChoiceField(label = 'Location', choices=location_list)
    scope_list = [('Individual', 'Individual'), ('Organization', 'Organization')]
    scope = forms.ChoiceField(label = 'Sign Up as: ', choices=scope_list, widget=forms.RadioSelect(), required=True, initial='Individual')
