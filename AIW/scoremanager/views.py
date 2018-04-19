from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents
from .utils import get_events_participated, get_events_hosted, score_volunteer

class ScoreBoardView(TemplateView):
    template_name = 'scoreboard.html'

    def get(self, request, *args, **kwargs):
        email_address = request.session['email_address']
        events_participated, total_score = get_events_participated(email_address)
        hosted_events = get_events_hosted(email_address)
        context = {
            'events_participated' : events_participated,
            'total_score' : total_score,
            'hosted_events' : hosted_events
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        email_address = request.session['email_address']
        volunteer_email, event_id = request.POST.get("event_id", "").split(":")
        score_volunteer(volunteer_email, event_id)
        events_participated, total_score = get_events_participated(email_address)
        hosted_events = get_events_hosted(email_address)
        context = {
            'events_participated' : events_participated,
            'total_score' : total_score,
            'hosted_events' : hosted_events
        }
        return render(request, self.template_name, context=context)
