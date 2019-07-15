from rest_framework import serializers
from .models import HouseImage, HouseRent

class HouseRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseRent
        fields = (
            'id','title', 'description',
            'bedroom_number', 'bathroom_number',
            'construcction_size', 'solar_size',
            'price', 'city'
        )

class HouseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = (
            'property_id',
            'image'
        )