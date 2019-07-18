from rest_framework import generics, viewsets, mixins
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
    # TODO dont allow list, retrive, delete