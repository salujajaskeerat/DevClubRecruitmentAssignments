# Generated by Django 3.0.4 on 2020-03-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0015_auto_20200325_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
