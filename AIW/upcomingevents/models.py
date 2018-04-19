from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.TextField()
    event_type = models.CharField(max_length=50)
    host_email = models.CharField(max_length=320)
    location = models.CharField(max_length=50)
    date = models.DateTimeField()
    score = models.IntegerField()
    volunteers_required = models.IntegerField()
    volunteers_registered = models.IntegerField(default = 0)
    no_of_days = models.IntegerField(default = 1)
    hours_per_day = models.IntegerField(default = 2)
