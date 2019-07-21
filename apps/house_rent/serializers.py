from rest_framework import serializers
from .models import HouseImage, House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = (
            'id','title', 'description',
            'bedroom_number', 'bathroom_number',
            'construcction_size', 'solar_size',
            'price', 'city', 'propietary', 'deleted'
        )

class HouseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = (
            'property_place',
            'image'
        )