from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    path = models.CharField(max_length=60)
    datetime = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
