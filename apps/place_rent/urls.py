from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'houses', views.HouseRentView)
router.register(r'houseimages', views.HouseImageView)

urlpatterns = [
    path('', include(router.urls))
]
