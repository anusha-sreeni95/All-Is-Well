from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .utils import save_details, new_user
from loginmanager.utils import add_session

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
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email_address = form.cleaned_data['email_address']
            password = form.cleaned_data['password']
            interests = form.cleaned_data['interests']
            location = form.cleaned_data['location']

            if(new_user(email_address)):
                save_details(full_name, phone_number, email_address, password, interests, location)
                add_session(request, email_address)
                return HttpResponseRedirect("/homepage")
            else:
                context = {
                    'form_class' : form_class,
                    'invalid'    : True,
                    'message' : 'User already exists'
                }
                return render(request, self.template_name, context=context)
        else:
            context = {
                'form_class' : form_class,
                'invalid'    : True,
                'message' : 'Invalid form entry'
            }
            return render(request, self.template_name, context=context)
