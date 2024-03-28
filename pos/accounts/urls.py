from django.urls import path
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
