from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'text', 'video', 'tag', 'timestamp')
