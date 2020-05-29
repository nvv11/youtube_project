from django.contrib import admin
from youtube.models import Video, Comment

admin.site.register([Video, Comment])
