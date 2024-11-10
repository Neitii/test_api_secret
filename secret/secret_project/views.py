from django.shortcuts import render
from rest_framework import filters, status, viewsets
from django.shortcuts import get_object_or_404
#from rest_framework.permissions import Allowany
from rest_framework.response import Response

from .models import Secret
from .serializers import SecretSerializer


class GenerateViewSet(viewsets.ModelViewSet):

    serializer_class = SecretSerializer
    http_method_names = ('post',)

    # def perform_create(self, serializer):
    #     """Создать отзыв к title_id."""
    #     secret_key = '222'

    #     serializer.save(
    #         secret_key=secret_key)
        
    def create(self, request, *args, **kwargs):
        """Переопределяем метод создания для возврата secret_key."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        # Возвращаем только secret_key вместо стандартного ответа
        secret_key = '333'
        serializer.save(
            secret_key=secret_key)
        return Response({"secret_key": secret_key}, status=status.HTTP_201_CREATED)

