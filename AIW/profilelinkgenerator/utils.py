from profilelinkgenerator.models import UrlTokens
from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents

def get_email_address(token):
    if(UrlTokens.objects.filter(token=token).exists()):
        return UrlTokens.objects.filter(token=token)[0].email_address
    else:
        return None

def events_participated(email_address):
    registered_events = RegisteredEvents.objects.filter(volunteer_email = email_address)
    participated_events=[]
    total_score = 0
    for event in registered_events:
        if(event.score!=0):
            rows = Event.objects.filter(id=event.event_id)
            for row in rows:
                participated_events.append({'event_name':row.event_name, 'description':row.description, 'date':row.date, 'location':row.location, 'score':event.score})
                total_score+=event.score
    return participated_events, total_score

def events_hosted(email_address):
    hosted_events = Event.objects.filter(host_email = email_address)
    events = []
    for event in hosted_events:
        events.append({'event_name':event.event_name, 'description':event.description, 'date':event.date, 'location':event.location})
    return events
