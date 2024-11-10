from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import status
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import Secret


class GenerateSerializer(serializers.ModelSerializer):
    """api_foodgram: сериализатор секретов"""

    class Meta:

        model = Secret
        exclude = ("pub_date", "secret_key")


class SecretSerializer(serializers.ModelSerializer):
    """api_foodgram: сериализатор секретов"""

    def validate(self, data):
        passphrase = data.get('passphrase')
        secret_key = data.get('secret_key')
        try:
            secret = Secret.objects.get(passphrase=passphrase, secret_key=secret_key)
        except Secret.DoesNotExist:
            raise serializers.ValidationError('Не верно')

        data['secret'] = secret.secret
        return data
  
    class Meta:

        model = Secret
        fields = ("passphrase", "secret_key")