from django.urls import path

from . import views
from .views import *

app_name = 'wellwash'
urlpatterns = [
    path('', index, name='index'),

    path('branches/', branch, name='branch'),
    path('branch_list/', branch_list, name='branch_list'),
    path('branch_list_view/', BranchListView.as_view(), name='branch_list_view'),
    path('branches/<int:pk>/', branch_detail, name='branch_detail'),

    path('washers/', washers_list, name='washer'),
    path('washers/<int:pk>/', washer_detail, name='washer_detail'),

    path('contact/', order_list, name='order_list'),

    path('coupons/', coupon, name='coupon'),

    path('cars/', car, name='car'),
    path('car/<str:add>', add_car, name='add_car'),

    path('coupons/<str:add>', add_coupon, name='add_coupon'),

    path('orders/', order, name='order'),
    path('order/<str:add>/', add_order, name='make_order'),
    path('order/<int:pk>/', make_order, name='make_order'),
]
