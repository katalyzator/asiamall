from django.conf.urls import url, include
from rest_framework import routers

from entertainments.api import EntertainmentViewSet
from entertainments.views import detail_entertainment_view

router = routers.DefaultRouter()
router.register(r'list', EntertainmentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^detail_entertainment_view/$', detail_entertainment_view),
]
