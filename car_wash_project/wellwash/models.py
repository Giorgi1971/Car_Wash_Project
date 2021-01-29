# Create your models here.
from .choices import *
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    zip = models.CharField(max_length=4)

    def __str__(self):
        # return self.street_address
        return f'{self.city}.  {self.street_address}'


class WashObject(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', unique=True)
    location = models.OneToOneField('wellwash.Location', on_delete=models.PROTECT, related_name='wash_object')

    def __str__(self):
        return self.title


class WashBox(models.Model):
    wash_object = models.ForeignKey(WashObject, on_delete=models.CASCADE, related_name='show_boxes')
    box_status = models.CharField(max_length=255)
    box_code = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return f'{self.box_code}  from -  {self.wash_object}'


class WashWasher(models.Model):
    full_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=11, unique=True)
    wash_object = models.ForeignKey(WashObject, on_delete=models.CASCADE, related_name='show_washers')

    def __str__(self):
        return f'{self.full_name} - {self.id_number}'


class Cars(models.Model):
    cars_model = models.CharField(max_length=255, default="BMW")
    cars_number = models.CharField(max_length=255, default='BMW-111', unique=True)
    cars_type = models.PositiveSmallIntegerField("CarType", choices=TypeChoices.choices, default=TypeChoices.Sedan)
    cars_color = models.PositiveSmallIntegerField('Color', choices=ColorChoices.choices, default=ColorChoices.White)

    def __str__(self):
        return f'{self.cars_model} : {self.cars_number}: {self.cars_type}'


class Order(models.Model):
    washer_id = models.ForeignKey(WashWasher, on_delete=models.PROTECT, related_name='orders')
    box_id = models.ForeignKey(WashBox, on_delete=models.PROTECT, related_name='orders')
    car_id = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name='orders')
    order_time = models.DateTimeField(verbose_name="Order time", blank=False,)
    start_time = models.DateTimeField(verbose_name="Begin time", blank=True,)
    end_time = models.DateTimeField(verbose_name="End time", blank=True)
    status = models.PositiveSmallIntegerField("Statuses", choices=StatusChoices.choices, default=StatusChoices.open)

    def __str__(self):
        return f'{self.pk} - {self.washer_id.full_name} - {self.box_id} - {self.car_id.cars_number}- {self.status}- {self.end_time}'

    def get_quantity_closed(self):
        pass

    def create_order(self):
        pass

    def close_order(self):
        pass

    def wash_price(self, pk):
        pass


# class Student(models.Model):
#     FRESHMAN = 'FR'
#     SOPHOMORE = 'SO'
#     JUNIOR = 'JR'
#     SENIOR = 'SR'
#     GRADUATE = 'GR'
#     YEAR_IN_SCHOOL_CHOICES = [
#         (FRESHMAN, 'Freshman'),
#         (SOPHOMORE, 'Sophomore'),
#         (JUNIOR, 'Junior'),
#         (SENIOR, 'Senior'),
#         (GRADUATE, 'Graduate'),
#     ]
#     year_in_school = models.CharField(
#         max_length=2,
#         choices=YEAR_IN_SCHOOL_CHOICES,
#         default=FRESHMAN,
#     )or1
#
#     def __str__(self):
#         return self.year_in_school
#
#     def is_upperclass(self):
#         return self.year_in_school in {self.JUNIOR, self.SENIOR}
