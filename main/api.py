from rest_framework import viewsets

from main.serializers import *


class AboutViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    http_method_names = ['get']

    def get_queryset(self):
        try:
            return AboutAsiaMall.objects.all()
        except:
            return {
                "result": None
            }


class AdvertiserViewSet(viewsets.ModelViewSet):
    serializer_class = AdvertiserSerializer
    http_method_names = ['get']

    def get_queryset(self):
        try:
            return Advertiser.objects.all()
        except:
            return {
                "result": None
            }


class LesseeViewSet(viewsets.ModelViewSet):
    serializer_class = LesseeSerializer
    http_method_names = ['get']

    def get_queryset(self):
        try:
            return Lessee.objects.all()
        except:
            return {
                "result": None
            }
