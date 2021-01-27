from django.urls import path
from .views import *

app_name = 'wellwash'

urlpatterns = [
    path('', index, name='index'),
    path('locations/', locations, name='locations'),
    path('locations/<int:location_id>/boxes/', location, name='location'),
    path('pp/', washer, name='washer5'),
    path('cars/', CarsView.as_view(), name='cars'),
    path('car/', car, name='car'),
    path('results/', WashObjectView.as_view(), name='results'),
    # path('<int:question_id>/', views.vote, name='vote'),
    path('view/', OrderView.as_view(), name='order'),
]