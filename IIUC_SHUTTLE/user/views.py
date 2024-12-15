from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UserRegistrationForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddDriverForm, RemoveDriverForm
from .models import Driver
from .models import Route


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = user.password  
            user.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('mail')
        password = request.POST.get('password')
        user = User.objects.filter(mail=email, password=password).first()
        if user:
            request.session['user_id'] = user.id
            messages.success(request, f'Welcome, {user.name}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')

def logout_user(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully.')
    return redirect('login')

def home(request):
    return render(request, 'home.html')


def manager_login_view(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        
        if (phone_number == settings.MANAGER_CREDENTIALS['phone_number'] and 
            password == settings.MANAGER_CREDENTIALS['password']):
            
            request.session['manager_logged_in'] = True
            messages.success(request, "Manager login successful.")
            return redirect('manager_dashboard')  
        else:
            messages.error(request, "Invalid phone number or password. Please try again.")
    
    return render(request, 'manager_login.html')

def manager_dashboard(request):
    if not request.session.get('manager_logged_in'):
        messages.error(request, "You must log in as a manager to access this page.")
        return redirect('manager_login')  
    
    return render(request, 'manager_dashboard.html')

def manager_logout_view(request):
    request.session.flush()  
    messages.success(request, "You have been logged out.")
    return redirect('manager_login')



def add_driver_view(request):
    if request.method == "POST":
        form = AddDriverForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Driver added successfully.")
            return redirect('manager_dashboard')
        else:
            messages.error(request, "Error adding driver. Please check the form.")
    else:
        form = AddDriverForm()
    return render(request, 'add_driver.html', {'form': form})

def remove_driver_view(request):
    if request.method == "POST":
        form = RemoveDriverForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            Driver.objects.filter(phone_number=phone_number).delete()
            messages.success(request, "Driver removed successfully.")
            return redirect('manager_dashboard')
        else:
            messages.error(request, "Error removing driver. Please check the form.")
    else:
        form = RemoveDriverForm()
    return render(request, 'remove_driver.html', {'form': form})

def add_route_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        start_location = request.POST.get('start_location')
        end_location = request.POST.get('end_location')
        scheduled_time = request.POST.get('scheduled_time')

        
        if Route.objects.filter(name=name).exists():
            messages.error(request, "Route with this name already exists.")
        else:
            
            Route.objects.create(
                name=name,
                start_location=start_location,
                end_location=end_location,
            )
            messages.success(request, "Route added successfully.")
            return redirect('manager_dashboard')

    return render(request, 'add_route.html')

def remove_route_view(request):
    if request.method == "POST":
        name = request.POST.get('name')

        
        if Route.objects.filter(name=name).exists():
            Route.objects.filter(name=name).delete()
            messages.success(request, f"Route '{name}' removed successfully.")
        else:
            messages.error(request, "Route not found.")

        return redirect('manager_dashboard')

    return render(request, 'remove_route.html')

from .forms import AddBusForm
from .models import Bus

def add_bus_view(request):
    if request.method == "POST":
        form = AddBusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bus added successfully.")
            return redirect('manager_dashboard')
        else:
            messages.error(request, "Error adding bus. Please check the form.")
    else:
        form = AddBusForm()
    return render(request, 'add_bus.html', {'form': form})

from .forms import RemoveBusForm
from .models import Bus

def remove_bus_view(request):
    if request.method == "POST":
        form = RemoveBusForm(request.POST)
        if form.is_valid():
            bus_number = form.cleaned_data['bus_number']
            Bus.objects.filter(bus_number=bus_number).delete()
            messages.success(request, f"Bus '{bus_number}' removed successfully.")
            return redirect('manager_dashboard')
        else:
            messages.error(request, "Error removing bus. Please check the form.")
    else:
        form = RemoveBusForm()
    return render(request, 'remove_bus.html', {'form': form})

def map_view(request):
    return render(request, 'map.html')

def map_check(request):
    return render(request, 'route_ceck.html')

def welcome(request):
    return render(request, 'welcome.html')