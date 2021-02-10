from datetime import datetime
from django.utils import timezone
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


class CarType(models.Model):
    class TypeChoices(models.TextChoices):
        SEDAN = 'SE', _('Sedan')
        JIP = 'JI', _('Jip')
        MINI = 'MI', _('Mini')
        TAXI = 'TA', _('Taxi')
        OTHER = 'OT', _('Other')

    car_type = models.CharField(
        max_length=2, choices=TypeChoices.choices, default=TypeChoices.SEDAN, verbose_name=_('Car Type'), unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.car_type


class Car(models.Model):
    cars_model = models.PositiveSmallIntegerField(verbose_name="Car Model",
                                                  choices=CarModelChoices.choices, default=CarModelChoices.mercedes)

    car_type = models.ForeignKey(to='CarType', on_delete=models.SET_NULL,
        null=True, related_name='car_car')
    licence_plate = models.CharField(max_length=24, default='CAR-000', unique=True)

    def __str__(self):
        return f'{self.cars_model} : {self.licence_plate}'

    def ct(self):
        pass


class WashType(models.Model):
    name = models.CharField(max_length=12, verbose_name=_('Wash Type'), unique=True)
    percentage = models.IntegerField(verbose_name=_("Percentage of base price"), default=100)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    code = models.CharField(max_length=5, unique=True)
    purchase_date = models.DateTimeField(verbose_name="purchase date", auto_now_add=True)
    discount = models.IntegerField(verbose_name=_('Discount'), help_text='%', default=20)
    validate = models.IntegerField(verbose_name=_('Validate period'), help_text='day', default=30)
    quantity = models.IntegerField(verbose_name=_('Quantity'), default=4)
    car_plate_id = models.OneToOneField(Car, on_delete=models.PROTECT, related_name='coupon')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('Coupon')
        verbose_name_plural = _('Coupons')


class Order(models.Model):
    car = models.ForeignKey(to='Car', on_delete=models.PROTECT, related_name='orders')

    employee = models.ForeignKey(
        to='user.User', on_delete=models.SET_NULL, null=True, related_name='orders')
    coupon = models.ForeignKey(
        to='Coupon', related_name='orders',
        on_delete=models.PROTECT,
        null=True, blank=True,
    )
    wash_type = models.ForeignKey(
        to='WashType', related_name='orders',
        on_delete=models.PROTECT,
    )
    box = models.ForeignKey(Box, on_delete=models.PROTECT, related_name='orders')
    my_wash_price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name=_("Price"))

    order_time = models.DateTimeField(verbose_name="Order time", auto_now_add=True)
    start_time = models.DateTimeField(verbose_name="Begin time", null=True)
    end_time = models.DateTimeField(verbose_name="End time", null=True)

    class StatusType(TextChoices):
        ordered = 'ordered', _("Ordered")
        process = 'process', _("Process")
        closed = 'closed', _("Closed")

    status = models.CharField(max_length=24, choices=StatusType.choices, default=StatusType.ordered)

    def __str__(self):
        return f'{self.car} using {self.wash_type}. status: {self.status}. - status: {self.my_wash_price}'

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.my_wash_price = self.car.car_type.price * self.wash_type.percentage / 100
        super(Order, self).save(*args, **kwargs)

    def get_quantity_closed(self):
        pass

    def create_order(self):
        pass

    def close_order(self):
        pass

    def wash_price(self, pk):
        pass
