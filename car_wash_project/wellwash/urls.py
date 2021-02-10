from django.urls import path

from . import views
from .views import *

app_name = 'wellwash'
urlpatterns = [
    path('', index, name='index'),
    path('washers/', washers_list, name='washers'),
    path('washerss/', washers_lists, name='washerss'),
    path('washers/<int:pk>/', washer_detail, name='washer_detail'),
    path('contact/', contact, name='contact'),
    path('coupons/', coupon, name='coupon'),
    path('cars/', views.CarView.as_view(), name='cars'),
    path('car/', car, name='car'),
    path('car/<str:add>', add_car, name='add_car'),
    path('order/', order5, name='order5'),
    path('order/<int:pk>/', make_order, name='make_order'),
]
