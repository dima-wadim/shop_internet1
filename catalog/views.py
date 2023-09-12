from django.shortcuts import render
import json
from catalog.models import Product, Contacts


def index(request):
    last_products = Product.objects.order_by('-date_create')[:5]
    for product in last_products:
        print(product.product_name)
    context = {"object_list": last_products}
    return render(request, 'catalog/home.html', context=context)

def contacts(request):
    contact_list = []
    if request.method == "POST":
        name = request.POST.get("name")
        ph_number = request.POST.get("phone")
        message = request.POST.get("message")
        Contacts.objects.create(contact_name=name, ph_number=ph_number, message=message)
    return render(request, 'catalog/contacts.html')
def product_detail(request, product_id):
    product = Product.objects.get(pk = product_id)
    context = {"object": product}
    return render(request, 'catalog/product.html', context=context)
