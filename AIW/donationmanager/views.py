from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import DonationForm
from .utils import create_donation
import datetime

class DonationView(FormView):
    form_class = DonationForm
    template_name = 'create_donation.html'

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = {
            'form_class' : form_class
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if(form.is_valid()):
            donation_title = form.cleaned_data['donation_title']
            donation_item_description = form.cleaned_data['donation_item_description']
            ngo_name = form.cleaned_data['ngo_name']
            location = form.cleaned_data['location']
            creation_date = datetime.datetime.now().date().strftime("%Y-%m-%d")
            ngo_email = request.session['email_address']

            create_donation(donation_title, donation_item_description, ngo_name, location, creation_date, ngo_email)
            return HttpResponseRedirect("/homepage")
        else:
            print("Error")
            context = {
                'form_class' : form_class,
                'invalid'    : True,
                'message' : 'Invalid form entry'
            }
            return render(request, self.template_name, context=context)
