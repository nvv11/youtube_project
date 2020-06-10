from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from youtube.views import HomeView, NewVideo, LoginView, RegisterView, VideoView, CommentView, VideoFileView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('new_video', NewVideo.as_view()),
    path('video/<int:id>', VideoView.as_view()),
    path('comment', CommentView.as_view()),
    path('videos/<file_name>', VideoFileView.as_view()),
    path('logout', LogoutView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('youtube_api.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
