from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [   
path('', views.home, name='home'),
path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),


]
