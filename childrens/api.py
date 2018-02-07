from rest_framework import viewsets

from childrens.models import Children
from childrens.serializers import ChildrenSerializer


class ChildrenViewSet(viewsets.ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer
    http_method_names = ['get', 'head']
