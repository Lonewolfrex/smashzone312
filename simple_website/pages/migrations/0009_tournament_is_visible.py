# Generated by Django 5.1 on 2024-09-05 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
    ]
