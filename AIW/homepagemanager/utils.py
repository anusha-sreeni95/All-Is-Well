from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents

def user_events_details(user_email_address):
    events_registered = RegisteredEvents.objects.filter(volunteer_email = user_email_address)
    events_participated = []
    for event in events_registered:
        #print(event.date)
        if(event.score==0):
            event_details = Event.objects.filter(id = event.event_id)
            for subevent in event_details:
                events_participated.append(subevent)
    print(events_participated)
    events_hosted = Event.objects.filter(host_email = user_email_address)
    return events_participated,events_hosted
