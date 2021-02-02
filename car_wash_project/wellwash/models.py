from .choices import *
# from django.forms import IntegerField
from django.db.models import IntegerChoices, TextChoices
from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    city = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    zip = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.city}.  {self.street_address}'


class Branch(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', unique=True)
    location_id = models.OneToOneField(to='wellwash.Location', on_delete=models.PROTECT, related_name='branch')

    def __str__(self):
        return self.title


class Box(models.Model):
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='boxes')
    box_code = models.CharField(max_length=12, unique=True)

    class BoxStatus(models.TextChoices):
        FREE = 'F', _("Free")
        BUSY = 'B', _("Busy")

    box_status = models.CharField(max_length=5, choices=BoxStatus.choices, default=BoxStatus.FREE)

    def __str__(self):
        return self.box_code


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    expiration_date = models.DateTimeField(verbose_name=_('Coupon Expiration Date'), null=True, blank=True)
    discount = models.IntegerField(verbose_name=_('Discount'), help_text='%')
    quantity = models.IntegerField(verbose_name=_('Quantity'), default=1)
    car_plate = models.CharField(max_length=20, verbose_name=_("Car's license plate"))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')


class Washer(models.Model):
    full_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=11, unique=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='washers')

    def __str__(self):
        return f'{self.full_name} - {self.id_number}  -  {self.branch_id}'


class Car(models.Model):
    cars_model = models.PositiveSmallIntegerField(verbose_name="CarModel",
                                                  choices=CarModelChoices.choices, default=CarModelChoices.mercedes)
    cars_type = models.CharField(max_length=10, verbose_name="CarType", choices=TypeChoices.choices, default=TypeChoices.Sedan)
    licence_plate = models.CharField(max_length=255, default='BMW-111', unique=True)

    def __str__(self):
        return f'{self.cars_model} : {self.licence_plate}: {self.cars_type}'


class Order(models.Model):
    washer_id = models.ForeignKey(Washer, on_delete=models.PROTECT, related_name='orders')
    box_id = models.ForeignKey(Box, on_delete=models.PROTECT, related_name='orders')
    car_id = models.ForeignKey(Car, on_delete=models.PROTECT, related_name='orders')
    order_time = models.DateTimeField(verbose_name="Order time", blank=False,)
    start_time = models.DateTimeField(verbose_name="Begin time", null=True)
    end_time = models.DateTimeField(verbose_name="End time", null=True)

    class Status(TextChoices):
        ordered = 'ordered', _("Ordered")
        process = 'process', _("Process")
        closed = 'closed', _("Closed")

    status = models.PositiveSmallIntegerField(choices=Status.choices)

    def __str__(self):
        return f'{self.car_id.licence_plate} - {self.status}'

    def get_quantity_closed(self):
        pass

    def create_order(self):
        pass

    def close_order(self):
        pass

    def wash_price(self, pk):
        pass
