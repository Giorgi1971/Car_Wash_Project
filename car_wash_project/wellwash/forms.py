from django import forms
from django.forms import EmailField, CharField

from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('wash_type', 'car')


class ContactForm(forms.Form):
    email = EmailField()
    body = CharField()
