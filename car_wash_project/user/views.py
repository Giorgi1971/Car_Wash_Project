from django.conf import settings
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
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


def user_registration(request):
    user_create_form = CustomUserCreationForm()
    if request.method == 'POST':
        user_create_form: CustomUserCreationForm = CustomUserCreationForm(request.POST, files=request.FILES)
        if user_create_form.is_valid():
            customer: User = user_create_form.save(commit=False)
            customer.status = User.Status.customer
            customer.save()
            return redirect('user:user_login')

    return render(
        request,
        template_name='user/registration.html',
        context={
            'form': user_create_form
        }
    )


def user_login(request):
    if request.user.is_authenticated:
        return redirect('wellwash:coupon')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('wellwash:branch')

    form = AuthenticationForm()
    return render(
        request,
        'user/login.html',
        context={
            'form': form
        }
    )


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)
    return HttpResponse(status=405)
