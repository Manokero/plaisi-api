from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tenant 
        fields = (
            'phone', 'address', 'province'
        )


class UserSerializer(serializers.ModelSerializer):
    tenant = TenantSerializer(required=False, many=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'password',
            'tenant',
        )
    
    def create(self, validated_data):
        pass
    
    def update(self, instance, validated_data):
        pass