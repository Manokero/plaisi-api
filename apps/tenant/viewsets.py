from rest_framework import viewsets, mixins, permissions
from .models import Tenant
from .serializers import TenantSerializer, UserSerializer
from django.contrib.auth.models import User


class TenantViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = TenantSerializer
    queryset = Tenant.objects.all()


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create' or self.action == 'update':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated&permissions.IsAdminUser]
            
        return [permission() for permission in permission_classes]