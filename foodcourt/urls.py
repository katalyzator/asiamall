from django.conf.urls import url, include
from rest_framework import routers

from foodcourt.api import FoodCourtViewSet

router = routers.DefaultRouter()
router.register(r'list', FoodCourtViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
