

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Staff, Role

def staff_list(request):
    staff_list = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {'staff_list': staff_list})

def add_staff(request):
    if request.method == 'POST':
        # Process form data and add staff member
        return redirect('staff_list')
    else:
        # Render form for adding staff member
        return render(request, 'staff/add_staff.html')

def edit_staff(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    if request.method == 'POST':
        # Process form data and edit staff member
        return redirect('staff_list')
    else:
        # Render form for editing staff member
        return render(request, 'staff/edit_staff.html', {'staff': staff})

def delete_staff(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'staff/delete_staff.html', {'staff': staff})

