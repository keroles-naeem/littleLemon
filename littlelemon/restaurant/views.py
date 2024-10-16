from os import login_tty
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,UserSerializer,BookingSerializer
from rest_framework import generics,viewsets,permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import status
from .forms import UserRegistrationForm,CustomLoginForm

# Create your views here. 

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login or success page
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
 
 
def login_page(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Corrected function call
            return redirect('home')  # Redirect to a success page
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})
 

 
class MenuItemsView(generics.ListCreateAPIView,generics.CreateAPIView):
   permission_classes = [IsAuthenticated]

   def post(self, request, *args, **kwargs):
      username = request.data.get('username')
      password = request.data.get('password')
      user = User.objects.filter(username=username).first()
      if user and user.check_password(password):
         token, created = Token.objects.get_or_create(user=user)
         return Response({'token': token.key}, status=status.HTTP_200_OK)
      return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
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
    
