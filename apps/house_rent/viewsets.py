from rest_framework import viewsets
from .models import HouseImage, House, HouseRent
from .serializers import (
        HouseImageSerializer, HouseSerializer
    )
from .filters import HouseFilter


class HouseRentView(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class HouseRentViewsetList(viewsets.ReadOnlyModelViewSet):
    queryset = House.objects.filter(
        deleted=False,
        propietary__user__is_active=True
    )
    serializer_class = HouseSerializer
    filterset_class = HouseFilter


class HouseImageView(viewsets.ModelViewSet):
    queryset = HouseImage.objects.all()
    serializer_class = HouseImageSerializer
