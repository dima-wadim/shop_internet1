from django.urls import path

from catalog.views import index, contacts, product_detail

urlpatterns = [
    path('', index),
    path('catalog/<int:product_id>/', product_detail),
    path('contacts', contacts)

]