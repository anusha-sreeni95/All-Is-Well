# Generated by Django 2.0.4 on 2018-04-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupmanager', '0004_auto_20180418_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='profile_photo',
            field=models.TextField(null=True),
        ),
    ]