from django.urls import path
from .views import *

app_name = 'wellwash'

urlpatterns = [
    path('', index, name='index'),
    path('branch/', branch, name='branch'),
    path('boxes/', box, name='box'),
    path('washers/', washer, name='washer'),
    path('order/', order, name='order'),


    # path('home/', home, name='home'),
    # path('car/', car, name='car'),

    # path('locations/<int:location_id>/boxes/', location, name='location'),
    # path('locations/boxes/<int:box_id>', box, name='box'),
    # path('locations/car/', car_type, name='car_type'),
    # path('cars/', CarsView.as_view(), name='cars'),
    # path('<int:question_id>/', views.vote, name='vote'),
]

# path('', IndexView.as_view(), name='index1'),
