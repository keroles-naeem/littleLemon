# /////////////////////////////////This File for Showing some cases and learning not executed in the app /////////////////////////////
# Certainly! Here’s how to handle token generation and validation using Django REST Framework's generic views.

# 1. Install Required Packages

# Ensure you have the necessary packages installed:

# pip install djangorestframework
# pip install djangorestframework-authtoken
# 2. Update settings.py

# Add the required apps to your INSTALLED_APPS:

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]
# 3. Create Token for Users Using Generic Views

# You can create a view to handle token generation using DRF's generic views. Here’s an example:

from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class CreateTokenView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
# 4. Protecting Views with Token Authentication

# You can use generic views to create protected endpoints. Here’s an example:

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ProtectedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({'message': 'This is a protected view!'})
# 5. URL Configuration

# Add the URLs for your token creation and protected views:

from django.urls import path
from .views import CreateTokenView, ProtectedView

urlpatterns = [
    path('api/token/', CreateTokenView.as_view(), name='create-token'),
    path('api/protected/', ProtectedView.as_view(), name='protected-view'),
]


# 6. Testing the API

# To Generate a Token: Send a POST request to /api/token/ with the username and password.
# To Access Protected View: Include the token in the Authorization header:
# Authorization: Token your_token_here
# This setup allows you to use Django REST Framework's generic views for token generation and validation.
# If you have any more questions or need further assistance, feel free to ask!

## Summary

# The token validation is not explicitly coded in the ProtectedView. Instead,
# it relies on the IsAuthenticated permission class to handle the validation process.
# If the token is valid, the user can access the view; if not, they receive an error response.
# If you have any more questions or need further clarification, feel free to ask!





# Coach
# Sure! Here’s a simple example of how to handle token generation and validation in a Django REST Framework project.

# 1. Install Required Packages

# Make sure you have Django and Django REST Framework installed, along with the token authentication package:

# pip install djangorestframework
# pip install djangorestframework-authtoken
# 2. Update settings.py

# Add the necessary apps to your INSTALLED_APPS:

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]
# 3. Create Token for Users

# You can create tokens for users using the Django shell or in your views. Here’s how to do it in a view:

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_token(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid Credentials'}, status=400)
# 4. Protecting Views with Token Authentication

# To protect your views, you can use the IsAuthenticated permission class:

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view!'})
# 5. URL Configuration

# Make sure to add the URLs for your token creation and protected views:

from django.urls import path
from .views import create_token, ProtectedView

urlpatterns = [
    path('api/token/', create_token, name='create-token'),
    path('api/protected/', ProtectedView.as_view(), name='protected-view'),
]
# 6. Testing the API

# To Generate a Token: Send a POST request to /api/token/ with the username and password.
# To Access Protected View: Include the token in the Authorization header as follows:
# Authorization: Token your_token_here
# This setup will allow you to generate and validate tokens for user authentication in your
# Django REST Framework application.
# If you have any more questions or need further assistance, feel free to ask!







# Djoser                 explan


# Here's a concise code example that illustrates how to use Djoser for user registration,
# login, and logout in a Django project.
# This will give you a good overview of how everything fits together.

# 1. Install Djoser

# Make sure you have Djoser installed:

# pip install djoser
# 2. Update settings.py

# Add Djoser to your installed apps and configure the REST framework:

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

DJOSER = {
    "USER_ID_FIELD": "username"
}
# 3. Update urls.py

# Include Djoser URLs in your project:

from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
# 4. User Registration

# To register a new user, send a POST request to /auth/users/ with the following JSON body:

{
    "username": "newuser",
    "password": "yourpassword"
}
# 5. User Login

# To log in, send a POST request to /auth/token/login/ with the following JSON body:

{
    "username": "newuser",
    "password": "yourpassword"
}
# You will receive a token in response,
# which you can use for authenticated requests.

# 6. User Logout

# To log out, send a POST request to /auth/token/logout/ with the token in the Authorization header:

# Authorization: Token your_token_here
# Summary

# Registration: Create a new user.
# Login: Authenticate and receive a token.
# Logout: Invalidate the token.
# This example provides a high-level overview of how to implement user
# authentication using Djoser in a Django application.
# If you have any questions or need further details, feel free to ask!
