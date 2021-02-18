# Generated by Django 3.1.6 on 2021-02-18 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wellwash', '0017_auto_20210215_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='user',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.PROTECT, related_name='user_coupon', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='box',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='wellwash.box'),
        ),
        migrations.AlterField(
            model_name='order',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='order',
            name='my_wash_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Begin time'),
            preserve_default=False,
        ),
    ]
