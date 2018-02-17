from rest_framework import serializers

from services.models import Service


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id', 'title', 'image', 'logo')
