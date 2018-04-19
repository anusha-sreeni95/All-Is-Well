from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents

def user_events_details(user_email_address):
    events_registered = RegisteredEvents.objects.filter(volunteer_email = user_email_address)
    print(events_registered)
    
    events_hosted = Event.objects.filter(host_email = user_email_address)
    
    return events_registered,events_hosted
	