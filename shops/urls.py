from django.conf.urls import url, include
from rest_framework import routers

from shops.api import ShopViewSet, CategoryViewSet, ShopListView

router = routers.DefaultRouter()
router.register(r'shopslist', ShopViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^filter_shop_by_category/(?P<category_id>\d+)/$', ShopListView.as_view()),
]
