# Generated by Django 3.1.5 on 2021-01-26 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars_model', models.CharField(max_length=255)),
                ('cars_number', models.CharField(max_length=255)),
                ('cars_type', models.PositiveSmallIntegerField(choices=[(1, 'Sedan'), (2, 'Jip'), (3, 'Mini')], default=1, verbose_name='CarType')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='WashObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Title')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='wash_object', to='wellwash.location')),
            ],
        ),
        migrations.CreateModel(
            name='WashWasher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('id_number', models.CharField(max_length=11, unique=True)),
                ('wash_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='show_washers', to='wellwash.washobject')),
            ],
        ),
        migrations.CreateModel(
            name='WashBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_status', models.CharField(max_length=255)),
                ('box_code', models.CharField(max_length=24, unique=True)),
                ('wash_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='box', to='wellwash.washobject')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Begin time')),
                ('end_time', models.DateTimeField(verbose_name='End time')),
                ('box_ordered', models.ManyToManyField(related_name='order_name', to='wellwash.WashBox')),
                ('washed_car', models.ManyToManyField(related_name='order_name', to='wellwash.Cars')),
                ('washers', models.ManyToManyField(related_name='order_name', to='wellwash.WashWasher')),
            ],
        ),
    ]
