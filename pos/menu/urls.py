# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('menu-management/', views.menu_management, name='menu_management'),
    path('add-menu-item/', views.add_menu_item, name='add_menu_item'),
    path('edit-menu-item/<int:item_id>/', views.edit_menu_item, name='edit_menu_item'),
    path('delete-menu-item/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),
]
