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
        context = {
            'form_class' : form_class
        }

        if(form.is_valid()):
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email_address = form.cleaned_data['email_address']
            password = form.cleaned_data['password']
            interests = form.cleaned_data['interests']
            location = form.cleaned_data['location']
            profile_photo = form.cleaned_data['profile_photo']
            gender = form.cleaned_data['gender']

            if(new_user(email_address)):
                save_details(full_name, phone_number, email_address, password, interests, location, profile_photo, gender)
            else:
                print("User already exists")
        return render(request, self.template_name, context=context)
