# Generated by Django 3.1.5 on 2021-02-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellwash', '0014_auto_20210211_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='activate_date',
            field=models.DateTimeField(verbose_name='activate_date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ordered', 'Ordered'), ('process', 'Process'), ('closed', 'Closed')], default='ordered', max_length=24),
        ),
    ]
