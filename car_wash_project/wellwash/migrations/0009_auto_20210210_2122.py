# Generated by Django 3.1.5 on 2021-02-10 21:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wellwash', '0008_auto_20210210_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='purchase_date',
        ),
        migrations.AddField(
            model_name='coupon',
            name='activate_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 10, 21, 22, 4, 577309, tzinfo=utc), verbose_name='Activate date'),
        ),
    ]
