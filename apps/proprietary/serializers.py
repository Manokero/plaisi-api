from collections import OrderedDict
from rest_framework import serializers
import json
from django.contrib.auth.models import User
from .models import Proprietary, ProprietaryLegalDoc

class ProprietarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Proprietary
        fields = (
            'phone', 'address', 'province'
        )


class ProprietarySerializerWithUser(serializers.ModelSerializer):

    class Meta:
        model = Proprietary
        fields = (
            'phone', 'address', 'province', 'user'
        )


class ProprietaryLegalDocSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProprietaryLegalDoc
        fields = (
            'document', 'name', 'description',
            'is_deleted', 'proprietary'
        )


class UserSerializer(serializers.ModelSerializer):
    proprietary = ProprietarySerializer(required=False, many=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'password',
           'proprietary',
        )
    
    def create(self, validated_data):
        proprietary_data = validated_data.pop('proprietary', OrderedDict())
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False
        
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        try:
            proprietary_data = json.loads(json.dumps(proprietary_data))
            user.proprietary_set.create(**proprietary_data)
        except:
            user.delete()

        return user
    
    def update(self, instance, validated_data):
        validated_data.pop('password', '')
        proprietary_data = validated_data.pop('proprietary', OrderedDict())
        proprietary_data = json.loads(json.dumps(proprietary_data))   
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False

        user = super(UserSerializer, self).update(
            instance, validated_data
        )
        user.proprietary_set.update(**proprietary_data)

        return user