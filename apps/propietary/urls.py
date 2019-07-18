from django.urls import path, include
from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'propietaries', viewsets.PropietaryViewSet)
router.register(r'userview', viewsets.UserView)

urlpatterns = [
    path('', include(router.urls)),
]
