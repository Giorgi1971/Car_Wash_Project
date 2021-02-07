from django.urls import path
from .views import *

app_name = 'wellwash'
urlpatterns = [
    path('', index, name='index'),
    path('washers/', washers_list, name='washers'),
    path('washers/<int:pk>/', washer_detail, name='washer_detail'),
]

