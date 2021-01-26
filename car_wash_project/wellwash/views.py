from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import WashObject, WashBox, WashWasher, Cars, Order, Location


def index(request):
    return HttpResponse("Hello. This is 'Cars Well Wash' site. <a href='locations'> See your locations</a>.")


def locations(request):
    # obj = WashObject.objects.all()
    # cont = {'cont': obj}
    return render(request, 'wellwash/index.html')


def washer(request):
    washer_list = WashWasher.objects.all()
    cont = {'cont': washer_list}
    return render(request, 'wellwash/index.html', cont)


class CarsView(generic.DetailView):
    model = Cars
    template_name = 'wellwash/models_view.html'


class WashObjectView(generic.DetailView):
    model = WashObject
    template_name = 'wellwash/models_view.html'


class OrderView(generic.DetailView):
    model = Order
    template_name = 'wellwash/models_view.html'
