from django.conf.urls import url, include
from rest_framework import routers

from foodcourt.api import FoodCourtViewSet
from foodcourt.views import detail_food_court_view

router = routers.DefaultRouter()
router.register(r'list', FoodCourtViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^detail_food_court_view', detail_food_court_view, name='detail_food_court_view'),
]
