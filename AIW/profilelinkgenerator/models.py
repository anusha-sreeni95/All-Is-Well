from django.db import models
from django.utils import timezone

class UrlTokens(models.Model):
    email_address = models.EmailField()
    token = models.TextField()
