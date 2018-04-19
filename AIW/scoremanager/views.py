from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents
from scoremanager.utils import *

class ScoreBoardView(TemplateView):
    template_name = 'scoreboard.html'

    def get(self, request, *args, **kwargs):
        user_email_address = request.session['email_address']
        events_participated,events_hosted,total_score,volunteers_per_event,score_received_per_event=user_events_details(user_email_address)
        context = {
            'events_registered' : events_participated,
            'events_hosted' : events_hosted,
            'total_score' : total_score,
            'volunteers_per_event' : volunteers_per_event,
            'score_received_per_event' : score_received_per_event
        }
        return render(request, self.template_name, context=context)
