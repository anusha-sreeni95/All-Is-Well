from django.db import models

class Event(models.Model):
    #event_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    event_type = models.CharField(max_length=50)
    host_email = models.CharField(max_length=320)
    location = models.CharField(max_length=50)
    date = models.DateTimeField()
    score = models.IntegerField()
    volunteers_required = models.IntegerField()

    
    def __str__(self):
        return self.title