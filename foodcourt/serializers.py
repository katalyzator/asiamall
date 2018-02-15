from rest_framework import serializers

from foodcourt.models import FoodCourt


class FoodCourtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodCourt
        fields = (
            'id', 'title', 'description', 'full_description', 'time_start', 'time_end', 'phone_number', 'facebook',
            'instagram', 'image', 'logo')
