from django.conf.urls import url, include
from rest_framework import routers

from promotions.api import PromotionViewSet

router = routers.DefaultRouter()
router.register(r'list', PromotionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
