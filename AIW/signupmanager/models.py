from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class UserData(models.Model):
    full_name = models.TextField()
    phone_number = models.TextField()
    email_address = models.EmailField(primary_key=True)
    password = models.TextField()
    environment = models.IntegerField(default = 0)
    education = models.IntegerField(default = 0)
    animal = models.IntegerField(default = 0)
    medical = models.IntegerField(default = 0)
    location = models.TextField(null = True)
    profile_photo = models.TextField(null = True)
    score = models.IntegerField(default = 0)
