from django.db import models

# Create your models here.
class DonationBox(models.Model):
    donation_title = models.CharField(max_length=200)
    donation_item_description = models.CharField(max_length=1000)
    ngo_name = models.CharField(blank=False,max_length=200)
    ngo_email = models.CharField(max_length=320)
    location = models.CharField(max_length=50)
    creation_date = models.DateTimeField()
