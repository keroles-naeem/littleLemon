from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem,Booking

 
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title','price','inventory']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name','no_of_guests','bookingDate']
       
