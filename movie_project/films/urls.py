from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.add_film, name='add_film')
]