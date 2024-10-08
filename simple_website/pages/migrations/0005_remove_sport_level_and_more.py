# Generated by Django 5.1 on 2024-09-01 04:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_sport_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='level',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favourite_sports',
        ),
        migrations.CreateModel(
            name='UserSport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('audience', 'Audience')], max_length=20)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.sport')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.userprofile')),
            ],
        ),
    ]
