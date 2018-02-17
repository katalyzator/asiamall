from rest_framework import serializers

from foodcourt.models import FoodCourt


class FoodCourtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodCourt
        fields = (
            'id', 'title', 'image', 'logo')
