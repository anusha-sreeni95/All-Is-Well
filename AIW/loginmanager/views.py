from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import LoginForm
from signupmanager.views import SignUpView
from .utils import verify_credentials

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

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
            email_address = form.cleaned_data['email_address']
            password = form.cleaned_data['password']

            if(verify_credentials(email_address, password)):
                print('Success')
            else:
                print('Invalid Creds')

            context = {
                'form_class' : form_class
            }
        return render(request, self.template_name, context=context)
