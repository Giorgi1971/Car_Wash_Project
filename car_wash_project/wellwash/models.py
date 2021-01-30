from .choices import *
from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    city = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    zip = models.CharField(max_length=4)

    def __str__(self):
        # return self.street_address
        return f'{self.city}.  {self.street_address}'


class Branch(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', unique=True)
    location_id = models.OneToOneField('wellwash.Location', on_delete=models.PROTECT, related_name='branch')

    def __str__(self):
        return self.title


class Box(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='boxes')
    box_code = models.CharField(max_length=12, unique=True)

    class BoxStatus(IntegerChoices):
        free = 1, _("Free")
        busy = 2, _("Busy")

    Box_status = models.PositiveSmallIntegerField(choices=BoxStatus.choices, default=1)

    def __str__(self):
        return f'{self.box_code}  from -  {self.branch_id}'


class Washer(models.Model):
    full_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=11, unique=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='washers')

    def __str__(self):
        return f'{self.full_name} - {self.id_number}'


class Car(models.Model):
    cars_type = models.PositiveSmallIntegerField("CarType", choices=TypeChoices.choices, default=TypeChoices.Sedan)
    cars_model = models.PositiveSmallIntegerField(
        "CarType", choices=CarModelChoices.choices, default=CarModelChoices.mercedes)
    cars_number = models.CharField(max_length=255, default='BMW-111', unique=True)

    def __str__(self):
        return f'{self.cars_model} : {self.cars_number}: {self.cars_type}'


class Order(models.Model):
    washer_id = models.ForeignKey(Washer, on_delete=models.PROTECT, related_name='orders')
    box_id = models.ForeignKey(Box, on_delete=models.PROTECT, related_name='orders')
    car_id = models.ForeignKey(Car, on_delete=models.PROTECT, related_name='orders')
    order_time = models.DateTimeField(verbose_name="Order time", blank=False,)
    start_time = models.DateTimeField(verbose_name="Begin time", null=True)
    end_time = models.DateTimeField(verbose_name="End time", null=True)

    class Status(IntegerChoices):
        ordered = 1, _("Ordered")
        process = 2, _("Process")
        closed = 3, _("Closed")

    status = models.PositiveSmallIntegerField(choices=Status.choices)

    def __str__(self):
        return f'{self.pk} - {self.washer_id.full_name} - {self.box_id} ' \
               f'- {self.car_id.cars_number}- {self.status}- {self.end_time}'

    def get_quantity_closed(self):
        pass

    def create_order(self):
        pass

    def close_order(self):
        pass

    def wash_price(self, pk):
        pass
