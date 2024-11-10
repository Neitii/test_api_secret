from django.contrib import admin
from django.urls import path

from secret_project.views import (GenerateAPIView, SecretsAPIView)

app_name = 'key'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('secrets/<str:key>/', SecretsAPIView.as_view(),
         name='secret'),
    path('generate/', GenerateAPIView.as_view(),
         name='generate'),
]
