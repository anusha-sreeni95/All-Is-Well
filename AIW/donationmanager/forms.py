from django import forms

class DonationForm(forms.Form):
    donation_title = forms.CharField(label='Title', max_length = 200)
    donation_item_description = forms.CharField(label='Description of Donation Accepted', max_length = 1000)
    ngo_name = forms.CharField(label='NGO Name', max_length = 200)
    location = forms.CharField(label = 'Location', max_length=50)
