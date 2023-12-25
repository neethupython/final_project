# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('department/<int:department_id>/', views.department_wikipedia, name='department_wikipedia'),
    path('new_page/', views.new_page, name='new_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('get_courses/', views.get_courses, name='get_courses'),
    # Add other URLs as needed
]
