# Generated by Django 3.1.5 on 2021-02-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellwash', '0012_auto_20210210_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='activate_date',
            field=models.DateTimeField(verbose_name='Activate date'),
        ),
    ]
