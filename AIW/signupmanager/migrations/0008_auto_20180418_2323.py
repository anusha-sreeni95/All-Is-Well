# Generated by Django 2.0.4 on 2018-04-18 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signupmanager', '0007_remove_userdata_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='education',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='environment',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='medical',
        ),
    ]