from rest_framework import viewsets

from foodcourt.models import FoodCourt
from foodcourt.serializers import FoodCourtSerializer


class FoodCourtViewSet(viewsets.ModelViewSet):
    queryset = FoodCourt.objects.all()
    serializer_class = FoodCourtSerializer
    http_method_names = ['get', 'head']
