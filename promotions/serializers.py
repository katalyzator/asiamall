from rest_framework import serializers

from news.serializers import TagSerializer
from promotions.models import Promotion


class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagSerializer(many=False, read_only=True)

    class Meta:
        model = Promotion
        fields = ('id', 'title', 'image', 'phone_number', 'text', 'share_url', 'tag', 'timestamp')
