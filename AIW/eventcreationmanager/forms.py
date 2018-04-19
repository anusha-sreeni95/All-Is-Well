from django import forms

class EventCreationForm(forms.Form):
    event_name = forms.CharField(label='Event Name', max_length = 200)
    description = forms.CharField(label='Description', max_length = 1000)
    event_type_list = [('Environment','Environment'), ('Education','Education'), ('Health Care','Health Care'), ('Animal Care', 'Animal Care')]
    event_type = forms.ChoiceField(label='Event Type', choices = event_type_list)
    location = forms.CharField(label = 'Location', max_length=50)
    start_date = forms.DateTimeField(label = 'Event Date', widget=forms.TextInput(attrs={'type': 'date'} ))
    volunteers_required = forms.IntegerField(label = 'Number of volunteers required')
    no_of_days = forms.IntegerField(label = 'Duration of event (days)')
    hours_per_day = forms.IntegerField(label = 'Hours to be spent per day on the event')
