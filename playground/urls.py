from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.index),
    path("home/", views.welcome),
]
