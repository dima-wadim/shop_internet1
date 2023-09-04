from django.urls import path

from config.catalog.views import index, contacts



urlpatterns = [
    path(' ', index),
    path('contacts', contacts)
]