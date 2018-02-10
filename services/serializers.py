from rest_framework import serializers

from services.models import Service


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'description', 'full_description', 'time_start', 'time_end', 'phone_number', 'image', 'logo')
