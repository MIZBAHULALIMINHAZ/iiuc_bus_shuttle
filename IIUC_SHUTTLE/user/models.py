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


class Route(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}: {self.start_location} → {self.end_location}"
    
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
