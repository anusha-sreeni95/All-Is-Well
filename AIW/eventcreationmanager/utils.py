from upcomingevents.models import Event

def create_event(event_name, description, event_type, location, start_date, volunteers_required, no_of_days, hours_per_day, host_email):
    score = no_of_days * hours_per_day * 2
    row = Event(event_name = event_name,
                description = description,
                event_type = event_type,
                host_email = host_email,
                location = location,
                date = start_date,
                score = score,
                volunteers_required = volunteers_required,
                no_of_days = no_of_days,
                hours_per_day = hours_per_day)
    row.save()
