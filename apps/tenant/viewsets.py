from rest_framework import viewsets, mixins, permissions
from .models import Tenant
from .serializers import TenantSerializer


class TenantViewset(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer