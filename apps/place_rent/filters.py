from django_filters import rest_framework as filters
from .models import HouseRent

class HouseFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_construction_size = filters.NumberFilter(
        field_name="construction_size", lookup_expr='gte')
    max_construction_size = filters.NumberFilter(
        field_name="construction_size", lookup_expr='lte')

    class Meta:
        model = HouseRent
        fields = ['city', 'min_price', 'max_price',
                  'min_construction_size', 'max_construction_size']