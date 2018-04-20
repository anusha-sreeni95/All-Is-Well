from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .utils import get_email_address
from signupmanager.models import UserData

class ProfilePage(TemplateView):
    template_name = 'profilepage.html'

    def get(self, request, token):
        print(token)
        email_address = get_email_address(token)
        if(email_address!=None):
            profile = UserData.objects.filter(email_address=email_address)[0]
            context = {
                'profile':profile
            }
            return render(request, self.template_name, context=context)
        else:
            return HttpResponseRedirect("/login")
