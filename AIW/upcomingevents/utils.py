from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents

def register_event(event_id,volunteer_email,score):
    row = RegisteredEvents(event_id = event_id,
                volunteer_email = volunteer_email,
                score = score)
    row.save()
    events = Event.objects.order_by('date')

def get_unregistered_events(user_email_address):
    events = Event.objects.order_by('date')
    unregistered_events=[]
    for event in events:
        row= RegisteredEvents.objects.filter(volunteer_email=user_email_address, event_id=event.id)
        if(len(row)==0):
            unregistered_events.append(event)
    return unregistered_events
