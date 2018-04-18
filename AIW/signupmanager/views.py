from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .utils import save_details, new_user

class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'signup.html'

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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email_address = form.cleaned_data['email_address']
            password = form.cleaned_data['password']

            if(new_user(email_address)):
                save_details(first_name, last_name, phone_number, email_address, password)
            else:
                print("User already exists")

            context = {
                'form_class' : form_class
            }
            return render(request, self.template_name, context=context)
