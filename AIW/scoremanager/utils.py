from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents
from signupmanager.models import UserData

def user_events_details(user_email_address):
    events_registered = RegisteredEvents.objects.filter(volunteer_email = user_email_address)
    events_participated = []
    total_score=0
    score_received_per_event=[]
    for event in events_registered:
        score_received_per_event.append(event.score)
        total_score+=event.score
        if(event.score!=0):
            event_details = Event.objects.filter(id = event.event_id)
            for subevent in event_details:
                events_participated.append(subevent)
    events_hosted = Event.objects.filter(host_email = user_email_address)
    volunteers_per_event=[]
    for event in events_hosted:
         volunteers=[]
         volunteer_rows = RegisteredEvents.objects.filter(event_id = event.id)
         for volunteer in volunteer_rows:
             volunteers.append(volunteer.volunteer_email)
         volunteers_per_event.append(volunteers)
    return events_participated,events_hosted,total_score,volunteers_per_event,score_received_per_event


def get_events_participated(email_address):
    registered_events = RegisteredEvents.objects.filter(volunteer_email = email_address)
    participated_events=[]
    total_score = 0
    for event in registered_events:
        row = Event.objects.filter(id=event.id)[0]
        participated_events.append({'event_name':row.event_name, 'description':row.description, 'date':row.date, 'location':row.location, 'score':event.score})
        total_score+=event.score
    return participated_events, total_score

def get_events_hosted(email_address):
    hosted_events = Event.objects.filter(host_email = email_address)
    events = []
    for event in hosted_events:
        rows = RegisteredEvents.objects.filter(event_id = event.id)
        volunteers = []
        for row in rows:
            volunteers.append(UserData.objects.filter(email_address = row.volunteer_email)[0].full_name)
        events.append({'event_name':event.event_name, 'description':event.description, 'date':event.date, 'location':event.location, 'volunteers':volunteers})
    return events
