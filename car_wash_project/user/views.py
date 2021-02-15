from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from django.core.mail import send_mail


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com',]
            if cc_myself:
                recipients.append(sender)
                print(recipients)

            print(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')

        return render(request, template_name='user/contact.html', context={
            'contact_form': form
        })
    else:
        form = ContactForm()
        return render(request, template_name='user/contact.html', context={
            'contact_form': form
        })


def staff(request):
    form = UserModelForms()
    return render(request, template_name='user/staff.html', context={
            'form': form
        })
