# Create your models here.
from django.db import models
from .choices import *


class Location(models.Model):
    city = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    zip = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.city} : {self.street_address}: {self.zip}'


class WashObject(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', unique=True)
    location = models.OneToOneField('wellwash.Location', on_delete=models.PROTECT, related_name='wash_object')

    def __str__(self):
        return self.title


class WashBox(models.Model):
    wash_object = models.ForeignKey(WashObject, on_delete=models.CASCADE, related_name='box')
    box_status = models.CharField(max_length=255)
    box_code = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return f'box# {self.box_code}  -   {self.wash_object}'


class WashWasher(models.Model):
    full_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=11, unique=True)
    wash_object = models.ForeignKey(WashObject, on_delete=models.CASCADE, related_name='show_washers')

    def __str__(self):
        return f'{self.full_name} - {self.id_number}'


class Cars(models.Model):
    cars_model = models.CharField(max_length=255)
    cars_number = models.CharField(max_length=255)
    cars_type = models.PositiveSmallIntegerField("CarType", choices=TypeChoices.choices, default=TypeChoices.Sedan)

    def __str__(self):
        return f'{self.cars_model} : {self.cars_number}'


class Order(models.Model):
    washers = models.ManyToManyField(to='wellwash.WashWasher', related_name='order_name')
    washed_car = models.ManyToManyField(to='wellwash.Cars', related_name='order_name')
    box_ordered = models.ManyToManyField(to='wellwash.WashBox', related_name='order_name')
    start_time = models.DateTimeField(verbose_name="Begin time", blank=True,)
    end_time = models.DateTimeField(verbose_name="End time", blank=True)
    status = models.CharField(max_length=24, default=None)

    def __str__(self):
        return f'{self.pk} - {self}'

    def get_quantity_closed(self):
        pass