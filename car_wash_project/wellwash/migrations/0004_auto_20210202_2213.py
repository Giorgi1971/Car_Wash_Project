# Generated by Django 3.1.5 on 2021-02-02 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wellwash', '0003_auto_20210201_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='cars_number',
            new_name='licence_plate',
        ),
    ]
