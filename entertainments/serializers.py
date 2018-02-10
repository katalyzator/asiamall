from rest_framework import serializers

from entertainments.models import Entertainment


class EntertainmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entertainment
        fields = ('id', 'title', 'description', 'full_description', 'time_start', 'time_end', 'phone_number', 'image')
