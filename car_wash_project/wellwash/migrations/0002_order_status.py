# Generated by Django 3.1.5 on 2021-01-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellwash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default=None, max_length=24),
        ),
    ]