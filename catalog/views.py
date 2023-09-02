from django.shortcuts import render

#from django.http import HttpResponse

def index(request):
    return render(request, 'catalog/control_1.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ph_number = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'Новое сообщение от  {name}({ph_number}): {message}')
    return render(request, 'catalog/control_2.html')