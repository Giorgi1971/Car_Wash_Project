from django.db.models import IntegerChoices, CharField


class TypeChoices(IntegerChoices):
    Sedan = 10
    Jip = 12
    Mini = 8
    Tax = 5


class ColChoices(CharField):
    White = 'White'
    Blue = 'Green'
    Green = 'Red'
    other = "Not published"


class ColorChoices(IntegerChoices):
    # (
    # (1, 'Male',),
    # (2, 'Female',),
    # (3, 'Other1',),
    # )
    White = 1
    Blue = 2
    Green = 3
    other = 4


class StatusChoices(IntegerChoices):
    open = 1
    proceed = 2
    close = 3
