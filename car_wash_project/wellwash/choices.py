from django.db.models import IntegerChoices
from django.utils.translation import gettext_lazy as _


class TypeChoices(IntegerChoices):
    Sedan = 1
    Jip = 2
    Mini = 3
    Tax = 4


class CarModelChoices(IntegerChoices):
    mercedes = 1, _('Mercedes')
    bmw = 2, _('BMW')
    lexus = 3, _('Lexus')
    kia = 4, _("Kia")
    subaru = 5, _("Subaru")
    mazda = 6, _('Mazda')
    skoda = 7, _('Skoda')
    toyota = 8, _('Toyota')
    honda = 9, _('Honda')
    peugeot = 10, _('Peugeot')
    volvo = 11, _('Volvo')


# class Status(IntegerChoices):
#         customer = 1, _("Customer")
#         washer = 2, _("Washer")
#         manager = 3, _("Manager")
#
#     status = models.PositiveSmallIntegerField(choices=Status.choices)
