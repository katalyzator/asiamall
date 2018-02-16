from rest_framework import serializers

from shops.models import Shop, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = (
            'id', 'title', 'description', 'full_description', 'like_counts', 'time_start', 'time_end', 'phone_number',
            'share_url',
            'instagram',
            'image', 'logo', 'category')
