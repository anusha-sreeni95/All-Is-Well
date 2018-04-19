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

    def post(self, request, *args, **kwargs):
        user_email_address = request.session['email_address']
        action=request.POST.get("event_id", "").split("_")[0]
        event_id=request.POST.get("event_id", "").split("_")[1]
        if(action=="unregister"):
            unregister_event(event_id,user_email_address,0)
        else:
            delete_event(event_id,user_email_address)
        events_registered, events_hosted = user_events_details(user_email_address)
        context = {
            'events_registered' : events_registered,
            'events_hosted' : events_hosted,
        }
        return render(request, self.template_name, context=context)

