from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .utils import user_events_details, unregister_event, delete_event, get_profile_link

class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        email_address = request.session['email_address']
        if(email_address!=''):
            events_registered, events_hosted = user_events_details(email_address)
            profile_link = get_profile_link(email_address)
            context = {
                'events_registered' : events_registered,
                'events_hosted' : events_hosted,
                'profile_link'   : profile_link
            }
            return render(request, self.template_name, context=context)
        else:
            return HttpResponseRedirect("/login")

    def post(self, request, *args, **kwargs):
        email_address = request.session['email_address']
        action=request.POST.get("event_id", "").split("_")[0]
        event_id=request.POST.get("event_id", "").split("_")[1]
        if(action=="unregister"):
            unregister_event(event_id, email_address, 0)
        else:
            delete_event(event_id, email_address)
        events_registered, events_hosted = user_events_details(email_address)
        context = {
            'events_registered' : events_registered,
            'events_hosted' : events_hosted,
        }
        return render(request, self.template_name, context=context)
