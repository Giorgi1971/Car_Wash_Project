from django.urls import path
from .views import *

app_name = 'wellwash'
urlpatterns = [
    path('washers/', washers_list, name='washers'),
    path('washers/<int:pk>/', washer_detail, name='washer'),
]

