from django.conf.urls import url, include
from rest_framework import routers

from news.api import NewsViewSet

router = routers.DefaultRouter()
router.register(r'newslist', NewsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
