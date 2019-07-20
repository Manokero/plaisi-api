from collections import OrderedDict
from rest_framework import serializers
import json
from django.contrib.auth.models import User
from .models import Propietary, PropietaryLegalDoc

class PropietarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Propietary
        fields = (
            'phone', 'address', 'province'
        )


class PropietarySerializerWithUser(serializers.ModelSerializer):

    class Meta:
        model = Propietary
        fields = (
            'phone', 'address', 'province', 'user'
        )


class PropietaryLegalDocSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropietaryLegalDoc
        fields = (
            'document', 'name', 'description',
            'is_deleted', 'propietary'
        )


class UserSerializer(serializers.ModelSerializer):
    propietary = PropietarySerializer(required=False, many=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'password',
           'propietary', 'is_staff', 'is_superuser'
        )
    
    def create(self, validated_data):
        propietary_data = validated_data.pop('propietary', OrderedDict())
        is_active = validated_data.get('is_active')
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False
        # If is_active attr inst sended, the default is True
        validated_data['is_active'] = True if is_active == None else is_active
        
        user = super(UserSerializer, self).create(validated_data)
        propietary_data = json.loads(json.dumps(propietary_data))
        user.propietary_set.create(**propietary_data)

        return user
    
    def update(self, instance, validated_data):
        validated_data.pop('password', '')
        propietary_data = validated_data.pop('propietary', OrderedDict())
        propietary_data = json.loads(json.dumps(propietary_data))   
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False

        user = super(UserSerializer, self).update(
            instance, validated_data
        )
        user.propietary_set.update(**propietary_data)

        return user