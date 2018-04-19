from django.db import models

class SessionData(models.Model):
    email_address = models.EmailField()
    ip_address = models.TextField()
