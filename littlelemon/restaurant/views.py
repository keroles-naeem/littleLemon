from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,UserSerializer,BookingSerializer
from rest_framework import generics,viewsets,permissions
from django.contrib.auth.models import User
# from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token
# Create your views here. 

 
class MenuItemsView(generics.ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = MenuItem.objects.all()
   serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
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
    
