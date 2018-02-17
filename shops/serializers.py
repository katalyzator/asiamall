from rest_framework import serializers

from shops.models import Shop, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class ShopSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'title', 'image', 'logo')
