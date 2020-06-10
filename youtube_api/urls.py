from django.urls import path
from youtube_api.views import VideoListView, CommentListView
urlpatterns = [
    path('videos', VideoListView.as_view(), name='videos.list'),
    path('comments', CommentListView.as_view(), name='comments.list'),
]
