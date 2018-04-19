from django.shortcuts import render
from django.views.generic import TemplateView
from homepagemanager.utils import user_events_details, unregister_event, delete_event, get_profile_link
from .utils import validate_token
from signupmanager.models import UserData

class ProfilePage(TemplateView):
    template_name = 'profilepage.html'

    def get(self, request, token):
        email_address = request.session['email_address']
        if(validate_token(token, email_address)):
            profile = UserData.objects.filter(email_address=email_address)[0]
            context = {
                'profile':profile
            }
            return render(request, self.template_name, context=context)
