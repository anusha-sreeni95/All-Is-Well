# Generated by Django 2.0.4 on 2018-04-18 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signupmanager', '0006_auto_20180418_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='profile_photo',
        ),
    ]
