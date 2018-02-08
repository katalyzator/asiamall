from rest_framework import viewsets

from entertainments.models import Entertainment
from entertainments.serializers import EntertainmentSerializer


class EntertainmentViewSet(viewsets.ModelViewSet):
    queryset = Entertainment.objects.all()
    serializer_class = EntertainmentSerializer
    http_method_names = ['get', 'head']
