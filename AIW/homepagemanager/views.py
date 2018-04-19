from django.shortcuts import render
from django.views.generic import TemplateView
from homepagemanager.utils import *

class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        user_email_address = request.session['email_address']
        events_registered, events_hosted = user_events_details(user_email_address)
        context = {
            'events_registered' : events_registered,
            'events_hosted' : events_hosted,
        }
        return render(request, self.template_name, context=context)
