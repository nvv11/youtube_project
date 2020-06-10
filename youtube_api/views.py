from rest_framework. generics import ListAPIView
from youtube.models import Video, Comment
from youtube_api.serializers import VideoSerializer, CommentSerializer


class VideoListView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
