from django.conf.urls import url, include
from rest_framework import routers

from services.api import ServiceViewSet

router = routers.DefaultRouter()
router.register(r'list', ServiceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
