from rest_framework import serializers

from shops.models import Shop, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = ('title', 'description', 'full_description', 'time_start', 'time_end', 'image', 'category')
