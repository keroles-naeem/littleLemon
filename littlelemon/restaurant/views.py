from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Menu
from .serializers import MenuItemSerializer
from rest_framework import generics
# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
        
def home(request):
 return render(request,"index.html",{})