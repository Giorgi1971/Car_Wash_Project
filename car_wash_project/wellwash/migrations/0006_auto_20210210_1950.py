# Generated by Django 3.1.5 on 2021-02-10 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wellwash', '0005_auto_20210207_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='expiration_date',
        ),
        migrations.AddField(
            model_name='coupon',
            name='purchase_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='purchase date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coupon',
            name='validate',
            field=models.IntegerField(default=30, help_text='day', verbose_name='Validate period'),
        ),
        migrations.AlterField(
            model_name='cartype',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(default=20, help_text='%', verbose_name='Discount'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='quantity',
            field=models.IntegerField(default=10, verbose_name='Quantity'),
        ),
    ]
