from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.staff_list, name='staff_list'),
    path('add/', views.add_staff, name='add_staff'),
    path('edit/<int:staff_id>/', views.edit_staff, name='edit_staff'),
    # Add more URL patterns as needed
]
