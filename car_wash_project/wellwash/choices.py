from django.db.models import IntegerChoices, CharField
from django.db import models


class TypeChoices(IntegerChoices):
    Sedan = 10
    Jip = 12
    Mini = 8
    Tax = 5


# class ColorChoices(CharField):
#     '''(
#         (1, 'Male',),
#         (2, 'Female',),
#         (3, 'Other1',),
#         )
#     '''
#     White = 'White'
#     Blue = 'Greeen'
#     Green = 'Reeed'
#     other = "Not published"
#

class ColorChoices(IntegerChoices):
    '''(
        (1, 'Male',),
        (2, 'Female',),
        (3, 'Other1',),
        )
    '''
    White = 1
    Blue = 2
    Green = 3
    other = 4


class StatusChoices(IntegerChoices):
    '''(
        (1, 'Male',),
        (2, 'Female',),
        (3, 'Other1',),
        )
    '''
    open = 1
    proceed = 2
    close = 3

