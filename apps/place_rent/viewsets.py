from rest_framework import viewsets
from .models import HouseImage, HouseRent
from .serializers import (
        HouseImageSerializer, HouseRentSerializer
    )
from .filters import HouseFilter


class HouseRentView(viewsets.ModelViewSet):
    queryset = HouseRent.objects.all()
    serializer_class = HouseRentSerializer


class HouseRentViewsetList(viewsets.ReadOnlyModelViewSet):
    queryset = HouseRent.objects.filter(
        deleted=False,
        propietary__user__is_active=True
    )
    serializer_class = HouseRentSerializer
    filterset_class = HouseFilter


class HouseImageView(viewsets.ModelViewSet):
    queryset = HouseImage.objects.all()
    serializer_class = HouseImageSerializer
