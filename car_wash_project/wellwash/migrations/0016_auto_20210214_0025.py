# Generated by Django 3.1.6 on 2021-02-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellwash', '0015_auto_20210212_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='image',
            field=models.ImageField(default='../static/wellwash/images/tb01.jpg', upload_to='profiles', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='phone_number',
            field=models.CharField(default=995577001, max_length=50, verbose_name='Phone Number'),
            preserve_default=False,
        ),
    ]
