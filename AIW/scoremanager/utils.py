from upcomingevents.models import Event
from homepagemanager.models import RegisteredEvents
from signupmanager.models import UserData

def get_events_participated(email_address):
    registered_events = RegisteredEvents.objects.filter(volunteer_email = email_address)
    participated_events=[]
    total_score = 0
    for event in registered_events:
        rows = Event.objects.filter(id=event.event_id)
        for row in rows:
            participated_events.append({'event_name':row.event_name, 'description':row.description, 'date':row.date, 'location':row.location, 'score':event.score})
        total_score+=event.score
    return participated_events, total_score

def get_events_hosted(email_address):
    hosted_events = Event.objects.filter(host_email = email_address)
    events = []
    for event in hosted_events:
        registered_participants = RegisteredEvents.objects.filter(event_id = event.id)
        volunteers = []
        for registered_participant in registered_participants:
            if(registered_participant.score!=0):
                not_scored = False
            else:
                not_scored = True
            user_details = UserData.objects.filter(email_address = registered_participant.volunteer_email)
            for user in user_details:
                volunteers.append({'email_address':user.email_address, 'name':user.full_name, 'not_scored': not_scored})
        events.append({'id':event.id, 'event_name':event.event_name, 'description':event.description, 'date':event.date, 'location':event.location, 'volunteers':volunteers})
    return events

def score_volunteer(volunteer_email, event_id):
    max_score = Event.objects.filter(id = event_id)[0].score
    score = max_score + UserData.objects.filter(email_address = volunteer_email)[0].score
    UserData.objects.filter(email_address = volunteer_email).update(score = score)
    RegisteredEvents.objects.filter(volunteer_email = volunteer_email, event_id = event_id).update(score = max_score)
