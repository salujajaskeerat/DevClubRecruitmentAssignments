# Generated by Django 3.0.4 on 2020-03-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0010_auto_20200324_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proff',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]