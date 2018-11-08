from django.urls import path
from .import views

urlpatterns = [
    path('', views.run_list, name='run_list'),
]