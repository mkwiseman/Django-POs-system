from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MenuItemForm
from .models import MenuItem
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



# views.py


def edit_menu_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu_management')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'menu/edit_menu_item.html', {'form': form})

def delete_menu_item(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_management')
    return render(request, 'menu/delete_menu_item.html', {'item': item})

