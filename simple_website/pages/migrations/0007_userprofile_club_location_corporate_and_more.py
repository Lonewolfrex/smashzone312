# Generated by Django 5.1 on 2024-09-05 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_userprofile_club_name_corporate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='club_location_corporate',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='club_location_society',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='club_location_sports',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
