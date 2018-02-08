from rest_framework import viewsets

from promotions.serializers import PromotionSerializer
from promotions.models import Promotion


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    http_method_names = ['get', 'head']
