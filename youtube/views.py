from django.shortcuts import render
from django.views.generic.base import View, HttpResponse


# Create your views here.

class Index(View):
    def get(self, request):
        return HttpResponse('Welcome to youtube_project!')
