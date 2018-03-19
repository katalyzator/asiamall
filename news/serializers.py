from rest_framework import serializers

from news.models import News, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)


class NewsSerializer(serializers.ModelSerializer):
    tag_name = serializers.RelatedField(source='tag', read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'text', 'video', 'tag_name', 'share_url', 'timestamp')
