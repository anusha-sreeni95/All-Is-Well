from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from upcomingevents.models import Event
from upcomingevents.utils import *
from donationmanager.models import DonationBox

class UpcomingEvents(TemplateView):
    template_name = 'features.html'

    def get(self, request, *args, **kwargs):
        user_email_address = request.session['email_address']
        events = get_unregistered_events(user_email_address)
        donations = DonationBox.objects.all()
        context = {'events': events, 'donations': donations}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        user_email_address = request.session['email_address']
        register_event((request.POST.get("event_id", "")),user_email_address,0)
        return HttpResponseRedirect("/homepage")
