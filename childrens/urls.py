from django.conf.urls import url, include
from rest_framework import routers

from childrens.api import ChildrenViewSet

router = routers.DefaultRouter()
router.register(r'childrenlist', ChildrenViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
