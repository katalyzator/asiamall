from rest_framework import serializers

from news.models import News, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)


class NewsSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(source='tag.title', read_only=True)
    timestamp = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'text', 'video', 'tag', 'share_url', 'timestamp')
