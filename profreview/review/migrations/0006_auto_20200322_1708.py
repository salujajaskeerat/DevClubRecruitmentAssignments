# Generated by Django 3.0.4 on 2020-03-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20200322_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default='default.png', upload_to=''),
        ),
    ]
