from django.shortcuts import render

# Create your views here.
# views.py
from .models import Category, MenuItem

def menu_management(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu_management.html', {'categories': categories})

def add_menu_item(request):
    if request.method == 'POST':
        # Process form data and add menu item
        # Redirect to menu management page after adding
    else:
        # Render form for adding menu item
        return render(request, 'menu/add_menu_item.html')
