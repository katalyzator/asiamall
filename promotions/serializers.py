from rest_framework import serializers

from news.serializers import TagSerializer
from promotions.models import Promotion


class PromotionSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(source='tag.title', read_only=True)
    timestamp = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Promotion
        fields = ('id', 'title', 'image', 'phone_number', 'text', 'share_url', 'tag', 'timestamp')
