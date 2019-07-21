from rest_framework import serializers
from collections import OrderedDict
from django.contrib.auth.models import User
import json
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
    # TODO: have in mind the Propietary User is alse a tenant
    def create(self, validated_data):
        tenant_data = validated_data.pop('tenant', OrderedDict())
        username = validated_data['username']
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False
        
        user = super(UserSerializer, self).create(validated_data)

        user.set_password(validated_data['password'])
        user.save()

        try:
            tenant_data = json.loads(json.dumps(tenant_data))
            user.tenant_set.create(**tenant_data)
        except:
            user.delete()

        return user
    
    def update(self, instance, validated_data):
        validated_data.pop('password', '')
        tenant_data = validated_data.pop('tenant', OrderedDict())
        tenant_data = json.loads(json.dumps(tenant_data))   
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False

        user = super(UserSerializer, self).update(
            instance, validated_data
        )
        user.tenant_set.update(**tenant_data)

        return user