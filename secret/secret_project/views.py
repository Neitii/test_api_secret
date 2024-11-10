from django.shortcuts import render
from rest_framework import filters, status, viewsets
from django.shortcuts import get_object_or_404
#from rest_framework.permissions import Allowany
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Secret
from .serializers import SecretSerializer, GenerateSerializer


class GenerateViewSet(viewsets.ModelViewSet):

    serializer_class = GenerateSerializer
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


# class SecretsViewSet(viewsets.ModelViewSet):

#     queryset = Secret.objects.all()
#     serializer_class = SecretSerializer
#     http_method_names = ['get', ]
#     #lookup_field = "id"

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         return Response(self.serializer_class(instance).data,
#                         status=status.HTTP_200_OK)


class SecretsAPIView(APIView):

    def post(self, request, key):
        # Используем ключ для поиска объекта
        try:
            secret = Secret.objects.get(id=key)  # Предполагается, что ключ - это id объекта
        except Secret.DoesNotExist:
            return Response({'error': 'Секрет не найден'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SecretSerializer(secret, data=request.data)
        
        if serializer.is_valid():
            secret = serializer.validated_data['secret']
            return Response({'secret': secret})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def delete(self, request):
    
