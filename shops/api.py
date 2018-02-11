from rest_framework import viewsets, generics

from shops.models import Shop, Category
from shops.serializers import ShopSerializer, CategorySerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    http_method_names = ['get', 'head']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'head']


class ShopListView(generics.ListAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category_filter = Category.objects.get(id=category_id)
        return Shop.objects.filter(category=category_filter)
