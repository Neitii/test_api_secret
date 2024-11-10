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


class SecretSerializer(serializers.ModelSerializer):
    """api_foodgram: сериализатор секретов"""

    class Meta:

        model = Secret
        exclude = ("pub_date", "secret_key")