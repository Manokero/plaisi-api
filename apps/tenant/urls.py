from django.urls import path, include
from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tenants', viewsets.TenantViewset)
router.register(r'tenant', viewsets.UserView)

urlpatterns = [
    path('', include(router.urls)),
]
