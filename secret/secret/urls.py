from rest_framework import routers

from django.contrib import admin
from django.urls import include, path

from secret_project.views import (GenerateViewSet,) #SecretsViewSet)

router = routers.DefaultRouter()
router.register(r'generate', GenerateViewSet, basename='generate')
#router.register(r'secrets', SecretsViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
