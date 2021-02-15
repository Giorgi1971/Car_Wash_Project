from django import forms
from django.forms import EmailField, CharField, IntegerField
from user.models import User
from .models import *


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('wash_type', 'car')


class CouponModelForm(forms.ModelForm):
    class Meta:
        widgets = {'activate_date': DateTimeInput()}
        model = Coupon
        fields = '__all__'


class OrderModelForm(forms.ModelForm):
    class Meta:
        widgets = {'end_time': DateTimeInput(), 'start_time': DateTimeInput(),}
        model = Order
        fields = '__all__'


class ContactForm(forms.Form):
    email = EmailField()
    body = CharField()


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class WasherForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
