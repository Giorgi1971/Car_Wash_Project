from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import WashObject, WashBox, WashWasher, Cars, Order, Location


def index(request):
    return HttpResponse("<h3>Welcome 'Well Wash'</h3><a href='locations'>locations</a><hr><a href='car'>cars</a>")


def locations(request):
    all_location = WashObject.objects.all()
    cont = {'cont': all_location}
    return render(request, 'wellwash/locations.html', cont)


def location(request, location_id):
    free_boxes = get_object_or_404(WashObject, pk=location_id).giorgi.filter(box_status='free')
    cont = {'cont': free_boxes}
    return render(request, 'wellwash/boxes.html', cont)


def box(request, box_id):
    free_boxes = get_object_or_404(WashBox, pk=box_id)
    cont = {'cont': free_boxes}
    return render(request, 'wellwash/box.html', cont)


def car_type(request):
    enter_car = Cars.objects.all()
    cont = {'cont': enter_car}
    return render(request, 'wellwash/car.html', cont)


def car(request):
    latest_cars_list = Cars.objects.all()[:10]
    output = ', '.join([c.cars_number for c in latest_cars_list])
    return HttpResponse(output)


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
