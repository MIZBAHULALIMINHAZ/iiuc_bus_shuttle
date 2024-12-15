# users/forms.py
from django import forms
from .models import Driver, User, Bus

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['id', 'name', 'number', 'mail', 'gender', 'usertype', 'password']

class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['phone_number', 'password']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if Driver.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already registered.")
        return phone_number
    
class RemoveDriverForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label="Phone Number")

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not Driver.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Driver with this phone number does not exist.")
        return phone_number
    

class AddBusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_number', 'capacity', 'bus_type']

class RemoveBusForm(forms.Form):
    bus_number = forms.CharField(max_length=20, label="Bus Number")

    def clean_bus_number(self):
        bus_number = self.cleaned_data.get('bus_number')
        if not Bus.objects.filter(bus_number=bus_number).exists():
            raise forms.ValidationError("Bus with this number does not exist.")
        return bus_number
    
from django import forms
from .models import Route

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['route_no', 'name', 'waypoints']
        widgets = {
            'waypoints': forms.Textarea(attrs={'placeholder': 'Enter waypoints as a JSON array, e.g., [[lat1, lon1], [lat2, lon2]]'}),
        }
