# Generated by Django 2.0.4 on 2018-04-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupmanager', '0013_userdata_profile_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='profile_link',
            field=models.TextField(),
        ),
    ]
