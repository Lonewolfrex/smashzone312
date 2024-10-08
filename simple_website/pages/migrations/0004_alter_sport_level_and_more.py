# Generated by Django 5.1 on 2024-09-01 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_sport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='level',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('audience', 'Audience')], max_length=20),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favourite_sports',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favourite_sports',
            field=models.ManyToManyField(to='pages.sport'),
        ),
    ]
