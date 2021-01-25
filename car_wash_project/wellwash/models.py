# Create your models here.
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    zip = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.city} : {self.street_address}: {self.zip}'


class WashObject(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    location = models.OneToOneField('wellwash.Location', on_delete=models.PROTECT, related_name='store')
    books = models.ManyToManyField(to='store.Book', blank=True, related_name='stores', through='store.StoreToBook')

    def __str__(self):
        return self.title