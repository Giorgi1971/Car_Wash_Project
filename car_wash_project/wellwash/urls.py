from django.urls import path
from . import views

app_name = 'wellwash'

urlpatterns = [
    path('', views.index, name='index'),
    path('locations/', views.locations, name='locations'),
    path('pp/', views.washer, name='washer5'),
    path('cars/', views.CarsView.as_view(), name='cars'),
    path('results/', views.WashObjectView.as_view(), name='results'),
    # path('<int:question_id>/', views.vote, name='vote'),
    path('view/', views.OrderView.as_view(), name='order'),
]