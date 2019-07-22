from rest_framework import viewsets, mixins, permissions
from .models import Proprietary, ProprietaryLegalDoc
from .serializers import (
        ProprietarySerializerWithUser, ProprietaryLegalDocSerializer,
        UserSerializer
    )
from django.contrib.auth.models import User


class ProprietaryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProprietarySerializerWithUser
    queryset = Proprietary.objects.filter(user__is_active=True)


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