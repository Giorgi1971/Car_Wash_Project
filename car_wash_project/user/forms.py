from django import forms
from .models import *
from .forms import *


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class CheckboxInput(forms.CheckboxInput):
    input_type = 'checkbox'


class UserModelForms(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
