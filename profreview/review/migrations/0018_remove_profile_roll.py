# Generated by Django 3.0.4 on 2020-03-26 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0017_profile_roll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='roll',
        ),
    ]
