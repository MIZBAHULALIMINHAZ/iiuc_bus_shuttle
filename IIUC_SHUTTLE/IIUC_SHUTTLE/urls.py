"""
URL configuration for IIUC_SHUTTLE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# user_management/urls.py
from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('home/', views.home, name='home'),
    path('manager-login/', views.manager_login_view, name='manager_login'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager-logout/', views.manager_logout_view, name='manager_logout'),
    path('add-driver/', views.add_driver_view, name='add_driver'),
    path('remove-driver/', views.remove_driver_view, name='remove_driver'),
    path('add-route/', views.add_route_view, name='add_route'),
    path('remove-route/', views.remove_route_view, name='remove_route'),
    path('add-bus/', views.add_bus_view, name='add_bus'),
    path('remove-bus/', views.remove_bus_view, name='remove_bus'),
    path('map/', views.map_view, name='map'),
    path('r/', views.map_check, name='mapd'),
]

