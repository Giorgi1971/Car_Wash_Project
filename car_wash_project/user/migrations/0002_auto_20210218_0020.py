# Generated by Django 3.1.6 on 2021-02-17 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salary',
            field=models.DecimalField(decimal_places=2, help_text='in Lari / % (if being washer )', max_digits=8, null=True, verbose_name='Salary'),
        ),
    ]
