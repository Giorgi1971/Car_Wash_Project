from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Branch, Box, Washer, Car, Order, Location


def index(request):
    return render(request, 'wellwash/index.html')


def branches(request):
    bs = Branch.objects.all()
    return render(request, 'wellwash/branches.html', {'many': bs})


class BranchView(generic.DetailView):
    model = Branch
    template_name = 'wellwash/branch.html'


def box(request):
    boxes = Box.objects.all()
    return render(request, 'wellwash/template.html', {'many': boxes})


def washer(request):
    washers = Washer.objects.all()
    return render(request, 'wellwash/template.html', {'many': washers})


def order(request):
    orders = Order.objects.all()
    return render(request, 'wellwash/template.html', {'many': orders})

#
# def home(request):
#     latest_cars_list = Car.objects.all()[:10]
#     data = [{"car": cc.cars_number} for cc in latest_cars_list]
#     return JsonResponse(data, safe=False)
#
#
# def car(request):
#     latest_cars_list = Car.objects.all()[:10]
#     data = [{"car": cc.cars_number} for cc in latest_cars_list]
#     return JsonResponse(data, safe=False)
#

# def box(request):
#     free_boxes = get_object_or_404(Box)
#     cont = {'cont': free_boxes}
#     return render(request, 'wellwash/box.html', cont)


# class IndexView(generic.ListView):
#     template_name = 'wellwash/index.html'
#     context_object_name = 'Wash_branch'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Branch.objects.all()


# def locations(request):
#     all_location = Branch.objects.all()
#     cont = {'cont': all_location}
#     return render(request, 'wellwash/locations.html', cont)


# def location(request, location_id):
#     free_boxes = get_object_or_404(Branch, pk=location_id).giorgi.filter(box_status='free')
#     cont = {'cont': free_boxes}
#     return render(request, 'wellwash/boxes.html', cont)

#
#
# def washer(request):
#     washer_list = Washer.objects.all()
#     cont = {'cont': washer_list}
#     return render(request, 'wellwash/index.html', cont)
#
#
# class CarsView(generic.DetailView):
#     model = Car
#     template_name = 'wellwash/models_view.html'
#
#
#
#
# def order(request):
#     model = Order
#     template_name = 'wellwash/models_view.html'
