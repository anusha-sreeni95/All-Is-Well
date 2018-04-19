from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from upcomingevents.models import Event

class UpcomingEvents(TemplateView):
    template_name = 'features.html'

    def get(self, request, *args, **kwargs):
        #form_class = self.get_form_class()
        #form = self.get_form(form_class)
        
        ##}
        events = Event.objects.order_by('date')
        print(events)
        context = {'events': events}
        return render(request, self.template_name, context=context)





#from django.shortcuts import render

# Create your views here.
#def event_list(request):
 #   return render(request, 'upcomingevents/features.html', {})

#from django.shortcuts import render

# Create your views here.
#def event_list(request):
#    return render(request, 'upcomingevents/features.html', {})