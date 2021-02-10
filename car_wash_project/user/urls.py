from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('contact_us/', contact_us, name='contact_us'),
]
