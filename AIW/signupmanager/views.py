from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import SignUpForm
from loginmanager.forms import LoginForm
from .utils import save_details, new_user, generate_profile_link
from loginmanager.utils import add_session

class SignUpView(FormView):
    login_form_class = LoginForm
    signup_form_class = SignUpForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'login_form_class' : self.login_form_class(request.GET),
            'signup_form_class' : self.signup_form_class(request.GET)
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        signup_form = self.signup_form_class(request.POST)

        if(signup_form.is_valid()):
            full_name = signup_form.cleaned_data['full_name']
            phone_number = signup_form.cleaned_data['phone_number']
            email_address = signup_form.cleaned_data['email_address']
            password = signup_form.cleaned_data['password']
            location = signup_form.cleaned_data['location']

            if(new_user(email_address)):
                profile_link = generate_profile_link(request, full_name, email_address, password)
                save_details(full_name, phone_number, email_address, password,  location, profile_link)
                add_session(request, email_address)
                return HttpResponseRedirect("/homepage")
            else:
                context = {
                    'login_form_class' : self.login_form_class(request.GET),
                    'signup_form_class' : self.signup_form_class(request.GET),
                    'signup_invalid'    : True,
                    'message' : 'User already exists'
                }
                return render(request, self.template_name, context=context)
        else:
            context = {
                'login_form_class' : self.login_form_class(request.GET),
                'signup_form_class' : self.signup_form_class(request.GET),
                'signup_invalid'    : True,
                'message' : 'Invalid form entry'
            }
            return render(request, self.template_name, context=context)
