from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import EventCreationForm
from .utils import create_event

class CreateEventView(FormView):
    form_class = EventCreationForm
    template_name = 'create_event.html'

    def get(self, request, *args, **kwargs):
        email_address = request.session['email_address']
        if(email_address!=''):
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            context = {
                'form_class' : form_class
            }
            return render(request, self.template_name, context=context)
        else:
            return HttpResponseRedirect("/login")

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if(form.is_valid()):
            event_name = form.cleaned_data['event_name']
            description = form.cleaned_data['description']
            event_type = form.cleaned_data['event_type']
            location = form.cleaned_data['location']
            start_date = form.cleaned_data['start_date']
            volunteers_required = form.cleaned_data['volunteers_required']
            no_of_days = form.cleaned_data['no_of_days']
            hours_per_day = form.cleaned_data['hours_per_day']
            host_email = request.session['email_address']

            create_event(event_name, description, event_type, location, start_date, volunteers_required, no_of_days, hours_per_day, host_email)
            return HttpResponseRedirect("/homepage")
        else:
            context = {
                'form_class' : form_class,
                'invalid'    : True,
                'message' : 'Invalid form entry'
            }
            return render(request, self.template_name, context=context)
