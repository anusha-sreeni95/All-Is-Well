from upcomingevents.models import Event
from .models import RegisteredEvents
from signupmanager.models import UserData

def user_events_details(user_email_address):
    events_registered = RegisteredEvents.objects.filter(volunteer_email = user_email_address)
    events_participated = []
    for event in events_registered:
        if(event.score==0):
            event_details = Event.objects.filter(id = event.event_id)
            for subevent in event_details:
                events_participated.append(subevent)
    events_hosted = Event.objects.filter(host_email = user_email_address)
    return events_participated,events_hosted

def unregister_event(event_id,volunteer_email,score):
    RegisteredEvents.objects.filter(event_id = event_id,
                volunteer_email = volunteer_email).delete()

def delete_event(event_id,volunteer_email):
    Event.objects.filter(id=event_id).delete()
    RegisteredEvents.objects.filter(event_id = event_id).delete()

def get_profile_link(email_address):
    return UserData.objects.filter(email_address=email_address)[0].profile_link
