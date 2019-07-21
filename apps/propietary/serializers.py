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
           'propietary',
        )
    
    def create(self, validated_data):
        propietary_data = validated_data.pop('propietary', OrderedDict())
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False
        
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

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