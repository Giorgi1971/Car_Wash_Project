from decimal import Decimal
from django.views.generic.list import ListView
from pyexpat import model
from typing import Dict, Optional
from django.core.paginator import Paginator
from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import F, Sum, ExpressionWrapper, DecimalField, Count, Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic

from .forms import *
from .models import *


# @TODO: Add Manager Method For Washer Listing

def index(request: WSGIRequest) -> HttpResponse:
    # if request.method == 'POST':
    return render(request=request, template_name='wellwash/index.html')


def add_coupon(request: WSGIRequest, add: str):
    coupon_add_form = CouponModelForm()
    if request.method == 'POST':
        coupon_add_form = CouponModelForm(request.POST)
        print(request.POST)
        if coupon_add_form.is_valid():
            print(coupon_add_form.cleaned_data)
            ord1: Coupon = coupon_add_form.save(commit=False)
            ord1.save()

        return redirect('wellwash:coupon')

    return render(request, template_name='wellwash/add_coup.html', context={
        'form': coupon_add_form
    })


def coupon(request: WSGIRequest) -> HttpResponse:
    coupon_q = Q()
    q1 = request.GET.get('coupon')
    if q1:
        coupon_q &= Q(code__icontains=q1)
    coupons_list = Coupon.objects.filter(coupon_q).order_by('-pk')
    paginator = Paginator(coupons_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request=request, template_name='wellwash/coupons.html', context=context)


class CarView(generic.ListView):
    template_name = 'wellwash/cars.html'
    context_object_name = 'Cars_list'
    car_form = CarModelForm()

    def get_queryset(self):
        """Return the last five published questions."""
        return CarModelForm


def washers_list(request: WSGIRequest) -> HttpResponse:
    washer_q = Q()
    order_q = Q()
    q = request.GET.get('washer')

    if q:
        washer_q &= Q(first_name__icontains=q) | Q(last_name__icontains=q)
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


class BranchListView(ListView):
    model = Branch

    def get_queryset(self):
        branch_list = Branch.objects.annotate(
        all_price=Sum('boxes__orders__my_wash_price')
        ).order_by('pk')
        return branch_list


def branch_list(request):
    branches = Branch.objects.annotate(
        all_price=Sum('boxes__orders__my_wash_price')
    )
    context = {'branch_list':branches.order_by('pk'),}
    return render(request=request, template_name='wellwash/branch_list.html', context=context)


def branch(request: WSGIRequest) -> HttpResponse:
    b_l = Branch.objects.all()
    order_info: Dict[str, Optional[Decimal]] = Branch.objects.annotate(
        branch_boxes=Count('boxes__box_code')
    ).annotate(
        mm=Sum('boxes__orders__my_wash_price')
    )
    print(type(order_info))
    context = {
        'branches': order_info.order_by('pk'),
    }
    return render(request=request, template_name='wellwash/branches.html', context=context)


def branch_detail(request: WSGIRequest, pk: int) -> HttpResponse:
    branch1 = get_object_or_404(Branch, pk=pk)
    now = timezone.now()
    branch_salary_info: Dict[str, Optional[Decimal]] = branch1.boxes.annotate(
        earned_per_order=Sum('orders__my_wash_price')).aggregate(
        earned_money_year=Sum(
            'earned_per_order',
            filter=Q(orders__end_time__gte=now - timezone.timedelta(days=365))
        ),
        washed_last_year=Count(
            'id',
            filter=Q(orders__end_time__gte=now - timezone.timedelta(days=365))
        ),
        earned_money_month=Sum(
            'earned_per_order',
            filter=Q(orders__end_time__gte=now - timezone.timedelta(weeks=4))
        ),
        washed_last_month=Count(
            'id',
            filter=Q(orders__end_time__gte=now - timezone.timedelta(weeks=4))
        ),
        earned_money_week=Sum(
            'earned_per_order',
            filter=Q(orders__end_time__gte=now - timezone.timedelta(days=7))
        ),
        washed_last_week=Count(
            'id',
            filter=Q(orders__end_time__gte=now - timezone.timedelta(days=7))
        )
    )
    bbb = branch1.boxes.annotate(nn=Count('id'))
    tt = Branch.objects.annotate(branch_boxes=Count('boxes'))
    n = tt.filter(id=pk)[0]

    return render(request, template_name='wellwash/branch_detail.html', context={
        'branch': branch1,
        'br': tt.filter(id=pk)[0],
        'bbb': bbb,
        **branch_salary_info,
    })


def order_list(request: WSGIRequest):
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
    cars_list = Car.objects.filter(plate_q).order_by('-pk')
    paginator = Paginator(cars_list, 7)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # mod = cars_list[0].cars_model.label
    context = {
        'page_obj': page_obj,
    }
    return render(request=request, template_name='wellwash/cars.html', context=context)


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


def make_order(request: WSGIRequest, pk: int):
    order_form = OrderModelForm2()
    pk = request.POST.get('pk')
    if request.method == 'POST':
        order_form = OrderModelForm2(request.POST)
        if order_form.is_valid():
            order1: Order = order_form.save(commit=False)
            order1.employee_id = pk
            order1.start_time = timezone.now()
            order1.save()

        return redirect('wellwash:index')

    return render(request, template_name='wellwash/save_form.html', context={
        'contact_form': order_form
    })


def add_order(request: WSGIRequest, add: str):
    order_form = OrderModelForm2()
    if request.method == 'POST':
        order_form = OrderModelForm2(request.POST)
        if order_form.is_valid():
            order1 = order_form.save(commit=False)
            order1.save()
            return redirect('wellwash:order')

    return render(request, template_name='wellwash/add-order-form.html', context={
        'order_form': order_form
    })


def order(request: WSGIRequest):
    order_q = Q()
    c1 = request.GET.get('order')
    if c1:
        order_q &= Q(car=c1)
        print(order_q)
    order_list = Order.objects.filter(order_q).order_by('-pk')
    paginator = Paginator(order_list, 5)  # Show 12 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    order_form = OrderModelForm2()

    # if request.method == 'POST':
    #     print('POST')
    #     coupon_form = CouponModelForm(request.POST)
    #     if coupon_form.is_valid():
    #         coupon1: Coupon = coupon_form.save(commit=False)
    #         coupon1.save()
    #
    #     return redirect('wash:washer-detail')

    context = {
        'form': order_form,
        'orders': order_list,
        'page_obj': page_obj,
    }

    return render(request=request, template_name='wellwash/orders.html', context=context)
