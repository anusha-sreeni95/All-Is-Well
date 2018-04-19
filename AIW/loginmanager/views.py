from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import LoginForm
from signupmanager.forms import SignUpForm
from signupmanager.views import SignUpView
from .utils import verify_credentials, add_session

class LoginView(FormView):
    login_form_class = LoginForm
    signup_form_class = SignUpForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        login_form = self.login_form_class(request.GET)
        signup_form_class = self.signup_form_class(request.GET)
        form = self.get_form(self.login_form_class)
        context = {
            'login_form_class' : self.login_form_class(request.GET),
            'signup_form_class' : self.signup_form_class(request.GET)
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        login_form = self.login_form_class(request.POST)

        if(login_form.is_valid()):
            email_address = login_form.cleaned_data['email_address']
            password = login_form.cleaned_data['password']

            if(verify_credentials(email_address, password)):
                add_session(request, email_address)
                request.session['email_address'] = email_address
                return HttpResponseRedirect("/homepage")
            else:
                context = {
                    'login_form_class' : self.login_form_class,
                    'invalid'    : True,
                    'message' : 'Please check the username and password'
                }
                return render(request, self.template_name, context=context)
        else:
            context = {
                'login_form_class' : self.login_form_class,
                'invalid'    : True,
                'message' : 'Invalid form entry'
            }
            return render(request, self.template_name, context=context)
