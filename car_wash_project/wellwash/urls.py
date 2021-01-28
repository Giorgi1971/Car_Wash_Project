from django.urls import path
from .views import *

app_name = 'wellwash'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', index1, name='index1'),
    path('locations/', locations, name='locations'),
    path('locations/<int:location_id>/boxes/', location, name='location'),
    path('locations/boxes/<int:box_id>', box, name='box'),
    path('locations/car/', car_type, name='car_type'),
    path('pp/', washer, name='washer5'),
    path('cars/', CarsView.as_view(), name='cars'),
    path('car/', car, name='car'),
    path('branches/<int:pk>', WashObjectView.as_view(), name='branch'),
    # path('<int:question_id>/', views.vote, name='vote'),
    path('view/', OrderView.as_view(), name='order'),
]