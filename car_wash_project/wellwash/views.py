from decimal import Decimal
from typing import Dict, Optional
from user.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import F, Sum, ExpressionWrapper, DecimalField, Count, Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# @TODO: Add Manager Method For Washer Listing
from django.views import generic

from .forms import ContactForm, OrderForm, OrderForm1, CarModelForm
from .models import *


# @TODO: Add Manager Method For Washer Listing

def index(request: WSGIRequest) -> HttpResponse:
    print('Giorgi')
    # if request.method == 'POST':
    return render(request=request, template_name='wellwash/index.html')


def coupon(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        print('Coupon')
        data = {'email': request.POST.get('email'), 'text': request.POST.get('body')}
        return render(request=request, template_name='wellwash/index.html', context=data)
    return render(request=request, template_name='wellwash/index.html')


class CarView(generic.ListView):
    template_name = 'wellwash/cars.html'
    context_object_name = 'Cars_list'
    car_form = CarModelForm()

    def get_queryset(self):
        """Return the last five published questions."""
        return CarModelForm


def add_car(request: WSGIRequest, add: str):
    car_add_form = CarModelForm()
    print(request.POST)
    if request.method == 'POST':
        car_add_form = CarModelForm(request.POST)
        if car_add_form.is_valid():
            car1: Car = car_add_form.save(commit=False)
            car1.save()

        return redirect('wellwash:car')

    return render(request, template_name='wellwash/add.html', context={
        'order_form': car_add_form
    })


def washers_list(request: WSGIRequest) -> HttpResponse:
    washer_q = Q()
    order_q = Q()
    q = request.GET.get('washer')

    if q:
        washer_q &= Q(first_name__icontains=q[-1]) | Q(last_name__icontains=q[-1])
        order_q &= Q(employee__first_name__icontains=q[-1]) | Q(employee__last_name__icontains=q[-1])

    profit_q = ExpressionWrapper(
        F('my_wash_price') * (1 - F('employee__salary') / Decimal('100.0')),
        output_field=DecimalField()
    )
    order_info: Dict[str, Optional[Decimal]] = Order.objects.filter(end_time__isnull=False).filter(order_q) \
        .annotate(profit_per_order=profit_q) \
        .aggregate(profit=Sum('profit_per_order'), total=Count('id'))

    context = {
        'washers': User.objects.filter(status=User.Status.washer.value).filter(washer_q).annotate(
            washed_count=Count('orders')),
        # **order_info
    }
    context.update(order_info)

    return render(request=request, template_name='wellwash/washers.html', context=context)


def washer_detail(request: WSGIRequest, pk: int) -> HttpResponse:
    washer: User = get_object_or_404(
        User.objects.filter(status=User.Status.washer.value),
        pk=pk
    )
    earned_money_q = ExpressionWrapper(
        F('my_wash_price') * F('employee__salary') / Decimal('100.0'),
        output_field=DecimalField()
    )
    now = timezone.now()
    washer_salary_info: Dict[str, Optional[Decimal]] = washer.orders.filter(end_time__isnull=False) \
        .annotate(earned_per_order=earned_money_q) \
        .aggregate(
        earned_money_year=Sum(
            'earned_per_order',
            filter=Q(end_time__gte=now - timezone.timedelta(days=365))
        ),
        washed_last_year=Count(
            'id',
            filter=Q(end_time__gte=now - timezone.timedelta(days=365))
        ),
        earned_money_month=Sum(
            'earned_per_order',
            filter=Q(end_time__gte=now - timezone.timedelta(weeks=4))
        ),
        washed_last_month=Count(
            'id',
            filter=Q(end_time__gte=now - timezone.timedelta(weeks=4))
        ),
        earned_money_week=Sum(
            'earned_per_order',
            filter=Q(end_time__gte=now - timezone.timedelta(days=7))
        ),
        washed_last_week=Count(
            'id',
            filter=Q(end_time__gte=now - timezone.timedelta(days=7))
        )
    )

    return render(request, template_name='wellwash/washer_detail.html', context={
        'washer': washer,
        **washer_salary_info
    })


def contact(request: WSGIRequest):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form.is_valid()
        contact_form = ContactForm(request.POST)
        # send_mail()
    return render(request, template_name='wellwash/contact.html', context={
            'contact_form': contact_form, 'email': request.POST.get('email'), 'text': request.POST.get('body')
        })


def car(request: WSGIRequest):
    plate_q = Q()
    q1 = request.GET.get('plate')
    if q1:
        plate_q &= Q(licence_plate__icontains=q1)
        print(plate_q)
    cars_list = Car.objects.filter(plate_q)
    paginator = Paginator(cars_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.POST:

        return render(request, 'wellwash/cars.html', {'page_obj': page_obj})

    context = {
        'cars': Car.objects.filter(plate_q),
        'page_obj': page_obj,
    }
    return render(request=request, template_name='wellwash/cars.html', context=context)


def order5(request: WSGIRequest):
    order_form = OrderForm1()
    if request.method == 'POST':
        order_form.is_valid()
        order_form = OrderForm1(request.POST)
        # send_mail()
    return render(request, template_name='wellwash/order.html', context={
        'order_form': order_form
    })


def make_order(request: WSGIRequest, pk: int):
    order_form = OrderForm()
    pk = request.POST.get('pk')
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order1: Order = order_form.save(commit=False)
            order1.employee_id = pk
            order1.start_time = timezone.now()
            order1.save()

        return redirect('wellwash:index')

    return render(request, template_name='wellwash/save_form.html', context={
        'contact_form': order_form
    })
