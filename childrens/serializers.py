from rest_framework import serializers

from childrens.models import Children


class ChildrenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Children
        fields = ('title', 'description', 'full_description', 'time_start', 'time_end', 'image')
