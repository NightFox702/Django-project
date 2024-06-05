from django.shortcuts import render
from .models import MenuItem

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'alcohol/menu.html', {'menu_items': menu_items})

def home(request):
    return render(request, 'alcohol/site.html')