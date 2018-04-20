from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .utils import get_email_address
from signupmanager.models import UserData
from .utils import events_participated, events_hosted

class ProfilePage(TemplateView):
    template_name = 'profilepage.html'

    def get(self, request, token):
        email_address = get_email_address(token)
        if(email_address!=None):
            profile = UserData.objects.filter(email_address=email_address)[0]
            participated, total_score = events_participated(email_address)
            hosted = events_hosted(email_address)
            context = {
                'profile':profile,
                'events_participated' : participated,
                'hosted_events' : hosted,
                'total_score' : total_score
            }
            return render(request, self.template_name, context=context)
        else:
            return HttpResponseRedirect("/login")
