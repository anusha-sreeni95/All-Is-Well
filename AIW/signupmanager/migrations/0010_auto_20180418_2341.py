# Generated by Django 2.0.4 on 2018-04-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupmanager', '0009_auto_20180418_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='animal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='education',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='environment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdata',
            name='medical',
            field=models.IntegerField(default=0),
        ),
    ]