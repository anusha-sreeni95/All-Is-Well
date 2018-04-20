from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents
from datetime import datetime
import pytz

def register_event(event_id,volunteer_email,score):
    row = RegisteredEvents(event_id = event_id,
                volunteer_email = volunteer_email,
                score = score)
    row.save()
    events = Event.objects.order_by('date')

def get_unregistered_events(user_email_address):
    events = Event.objects.order_by('date')
    unregistered_events=[]
    current_datetime=datetime.now()
    pytz.utc.localize(current_datetime)
    for event in events:
        if(event.date.replace(tzinfo=None)<current_datetime):
            print("Yess!")
        row= RegisteredEvents.objects.filter(volunteer_email=user_email_address, event_id=event.id)
        if(len(row)==0):
            unregistered_events.append(event)
    return unregistered_events
