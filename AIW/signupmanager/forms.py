from django import forms

class SignUpForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100, required=True)
    phone_number = forms.CharField(label='Phone Number', max_length=10, required=True)
    email_address = forms.EmailField(label='Email Address', max_length=254, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    interests_list = [('Environment', 'Environment'), ('Education', 'Education'), ('Animal','Animal'), ('Medical','Medical')]
    interests = forms.MultipleChoiceField(choices = interests_list, widget=forms.CheckboxSelectMultiple)
    location = forms.CharField(label = 'Location', required = False)
    profile_photo = forms.FileField(label = 'Profile Photo', required = False, widget = forms.ClearableFileInput(attrs={'multiple' : False}))
    gender_list = [('M','Male'), ('F','Female'), ('O','Other')]
    gender = forms.ChoiceField(choices = gender_list)
