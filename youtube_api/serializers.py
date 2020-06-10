from rest_framework import serializers
from youtube.models import Video, Comment


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'description', 'path', 'datetime', 'user')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'datetime', 'user', 'video')
