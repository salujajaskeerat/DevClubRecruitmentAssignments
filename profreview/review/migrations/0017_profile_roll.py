# Generated by Django 3.0.4 on 2020-03-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0016_auto_20200325_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='roll',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
