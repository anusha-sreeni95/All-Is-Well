# Generated by Django 2.0.4 on 2018-04-20 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilelinkgenerator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urltokens',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='urltokens',
            name='token',
            field=models.TextField(blank=True),
        ),
    ]