from django.urls import path
from . import views
rom django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'),
]
