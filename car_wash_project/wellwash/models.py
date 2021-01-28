# Create your models here.
from .choices import *
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    zip = models.CharField(max_length=4)

    def __str__(self):
        return self.street_address
        # return f'{self.city} : {self.street_address}: {self.zip}'


class WashObject(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', unique=True)
    location = models.OneToOneField('wellwash.Location', on_delete=models.PROTECT, related_name='wash_object')

    def __str__(self):
        return self.title


class WashBox(models.Model):
    wash_object = models.ForeignKey(WashObject, on_delete=models.CASCADE, related_name='giorgi')
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
    cars_model = models.CharField(max_length=255, default="bmw")
    cars_number = models.CharField(max_length=255, default='aaa-111')
    cars_type = models.PositiveSmallIntegerField("CarType", choices=TypeChoices.choices, default=TypeChoices.Sedan)
    cars_color = models.PositiveSmallIntegerField('Color', choices=ColorChoices.choices, default=ColorChoices.White)

    def __str__(self):
        return f'{self.cars_model} : {self.cars_number}: {self.cars_type}'


class Order(models.Model):
    washer = models.ForeignKey(WashWasher, on_delete=models.PROTECT, related_name='show_ord')
    washing_box = models.ForeignKey(WashBox, on_delete=models.PROTECT, related_name='show_ordd')
    washing_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name='show_orddd')
    start_time = models.DateTimeField(verbose_name="Begin time", blank=True,)
    end_time = models.DateTimeField(verbose_name="End time", blank=True)
    status = models.PositiveSmallIntegerField("Statuses", choices=StatusChoices.choices, default=StatusChoices.open)

    def __str__(self):
        return f'{self.pk} - {self.washer} - {self.washing_box} - {self.washing_car}- {self.status}- {self.start_time}'

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
