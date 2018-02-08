from rest_framework import serializers

from promotions.models import Promotion


class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promotion
        fields = ('id', 'title', 'image', 'text', 'tag', 'timestamp')
