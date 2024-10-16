from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [   
path('', views.home, name='home'),
path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
path('login/', views.login_page, name='login_page'),
path('registration/', views.register, name='registration')
]
