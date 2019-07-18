from rest_framework import generics, viewsets, mixins, permissions
from .models import Propietary, PropietaryLegalDoc
from .serializers import (
        PropietarySerializerWithUser, PropietaryLegalDocSerializer,
        UserSerializer
    )
from django.contrib.auth.models import User


class PropietaryViewSet(viewsets.ModelViewSet):
    serializer_class = PropietarySerializerWithUser
    queryset = Propietary.objects.filter(user__is_active=True)


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
            permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

        return [permission() for permission in permission_classes]