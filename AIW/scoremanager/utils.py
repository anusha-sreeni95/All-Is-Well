from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents
from signupmanager.models import UserData

def get_events_participated(email_address):
    registered_events = RegisteredEvents.objects.filter(volunteer_email = email_address)
    participated_events=[]
    total_score = 0
    for event in registered_events:
        rows = Event.objects.filter(id=event.id)
        for row in rows:
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
            users = UserData.objects.filter(email_address = row.volunteer_email)
            for user in users:
                volunteers.append({'email_address':row.volunteer_email, 'name':user.full_name})
        events.append({'id':event.id, 'event_name':event.event_name, 'description':event.description, 'date':event.date, 'location':event.location, 'volunteers':volunteers})
    return events

def score_volunteer(volunteer_email, event_id):
    max_score = Event.objects.filter(id = event_id)[0].score
    score = max_score + UserData.objects.filter(email_address = volunteer_email)[0].score
    UserData.objects.filter(email_address = volunteer_email).update(score = score)
    RegisteredEvents.objects.filter(volunteer_email = volunteer_email, event_id = event_id).update(score = max_score)
