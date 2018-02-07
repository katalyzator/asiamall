from django.conf.urls import url, include
from rest_framework import routers

from shops.api import ShopViewSet

router = routers.DefaultRouter()
router.register(r'shopslist', ShopViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
