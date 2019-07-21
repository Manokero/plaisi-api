from django.urls import path, include
from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'proprietaries', viewsets.ProprietaryViewSet)
router.register(r'proprietary', viewsets.UserView)

urlpatterns = [
    path('', include(router.urls)),
]
