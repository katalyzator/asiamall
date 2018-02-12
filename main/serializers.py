from rest_framework import serializers

from main.models import AboutAsiaMall, Lessee, Advertiser


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutAsiaMall
        fields = ('id', 'title', 'text', 'timestamp')


class LesseeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lessee
        fields = ('id', 'title', 'phone_number1', 'phone_number2', 'email', 'text', 'timestamp')


class AdvertiserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advertiser
        fields = ('id', 'title', 'phone_number1', 'phone_number2', 'email', 'text', 'timestamp')
