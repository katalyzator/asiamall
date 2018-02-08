from django.conf.urls import url, include
from rest_framework import routers

from entertainments.api import EntertainmentViewSet

router = routers.DefaultRouter()
router.register(r'list', EntertainmentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
