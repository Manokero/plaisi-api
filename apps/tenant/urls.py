from django.urls import path, include
from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tenants', viewsets.TenantViewset)

urlpatterns = [
    path('', include(router.urls)),
]
