import hashlib
import base64

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Secret
from .serializers import SecretSerializer, GenerateSerializer


class GenerateAPIView(APIView):
    """secret: viewset создания записи."""

    def post(self, request):
        """Создание записи и возврат ссылки на запись."""
        serializer = GenerateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        # хешируем ссылку по id записи
        hash_object = hashlib.sha256(str(instance.id).encode())
        hash_bytes = hash_object.digest()
        encoded_hash = base64.urlsafe_b64encode(hash_bytes).decode('utf-8')
        hashed_link = encoded_hash.rstrip('=')
        secret_key = hashed_link

        instance.secret_key = secret_key
        instance.save()

        return Response({"secret_key": secret_key},
                        status=status.HTTP_201_CREATED)


class SecretsAPIView(APIView):
    """secret: viewset выдачи и удаления записи."""

    def post(self, request, key):
        """Возврат секрета и удаления записи."""
        serializer = SecretSerializer(data=request.data,
                                      context={'secret_key': key})

        if serializer.is_valid():
            secret = serializer.validated_data['secret']
            Secret.objects.filter(secret_key=key).delete()
            return Response({'secret': secret})

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
