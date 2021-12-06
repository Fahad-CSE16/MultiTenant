from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'driver', DriverViewSet)

urlpatterns = [
    path('', homeview, name="home"),
    path('create/', CreateDriver, name="createdriver"),
    path('', include(router.urls)),
]
