from django.conf.urls import url, include
from rest_framework import routers

from main.views import get_main_page_values
from promotions.api import PromotionViewSet

router = routers.DefaultRouter()
router.register(r'list', PromotionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^get_main_page_values/', get_main_page_values, name='get_main_page_values'),
]
