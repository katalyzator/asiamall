from django.conf.urls import url, include
from rest_framework import routers

from services.api import ServiceViewSet
from services.views import detail_service_view

router = routers.DefaultRouter()
router.register(r'list', ServiceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^detail_service_view/$', detail_service_view, name='detail_service_view'),

]