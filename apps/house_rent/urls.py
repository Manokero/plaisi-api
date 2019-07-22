from django.urls import path, include
from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'house', viewsets.HouseRentView)
router.register(r'houses', viewsets.HouseRentViewsetList)
router.register(r'houseimages', viewsets.HouseImageView)

urlpatterns = [
    path('', include(router.urls)),
]
