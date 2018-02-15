from django.conf.urls import url, include
from rest_framework import routers

from main.views import get_main_page_values, search_view, post_application
from main.api import *

router = routers.DefaultRouter()
router.register(r'about', AboutViewSet, base_name='About')
router.register(r'lessee', LesseeViewSet, base_name='Lessee')
router.register(r'advertiser', AdvertiserViewSet, base_name='Advertiser')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^get_main_page_values/', get_main_page_values, name='get_main_page_values'),
    url(r'^search/$', search_view),
    url(r'^post_application/$', post_application),
]
