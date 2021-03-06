from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('contact_us/', contact_us, name='contact_us'),
    path('staff/', staff, name='staff'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('registration/', user_registration, name='user_registration'),
]
