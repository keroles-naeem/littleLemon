from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Menu,Booking
from .serializers import MenuItemSerializer,UserSerializer,BookingSerializer
from rest_framework import generics,viewsets,permissions
from django.contrib.auth.models import User

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
        
def home(request):
 return render(request,"index.html",{})


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 
   
class BookingViewSet (viewsets.ModelViewSet):
    queryset= Booking.objects.all()
    serializer_class=BookingSerializer
    
