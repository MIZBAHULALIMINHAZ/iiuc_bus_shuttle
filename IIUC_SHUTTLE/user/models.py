from django.db import models

class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15, unique=True)
    mail = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    usertype = models.CharField(
        max_length=10,
        choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Staff', 'Staff')]
    )
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.name

class Driver(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number


    
class Bus(models.Model):
    BUS_TYPES = [
        ('IIUC', 'IIUC'),
        ('LOCAL', 'Local'),
    ]

    bus_number = models.CharField(max_length=20, unique=True)
    capacity = models.PositiveIntegerField()
    bus_type = models.CharField(max_length=10, choices=BUS_TYPES, default='LOCAL')

    def __str__(self):
        return f"Bus {self.bus_number} - {self.bus_type} - Capacity: {self.capacity}"
    
from django.db import models

class Route(models.Model):
    route_no = models.CharField(max_length=10, unique=True)  # Unique route number
    name = models.CharField(max_length=100)  # Route name or description
    waypoints = models.JSONField()  # List of coordinates

    def __str__(self):
        return f"Route {self.route_no}: {self.name}"
