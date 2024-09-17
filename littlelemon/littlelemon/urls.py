from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from restaurant import views


router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('restaurant/booking/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
