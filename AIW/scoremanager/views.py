from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents

class ScoreBoardView(TemplateView):
    template_name = 'scoreboard.html'

    def get(self, request, *args, **kwargs):
        user_email_address = request.session['email_address']
        events_registered = RegisteredEvents.objects.filter(volunteer_email = user_email_address)
        events_hosted = Event.objects.filter(host_email = user_email_address)
        context = {
            'events_registered' : events_registered,
            'events_hosted' : events_hosted
        }
        return render(request, self.template_name, context=context)
