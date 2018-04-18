from django.db import models

class UserData(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.TextField()
    email_address = models.EmailField(primary_key=True)
    password = models.TextField()
