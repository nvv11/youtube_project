from django.shortcuts import render
from django.views.generic.base import View, HttpResponse


# Create your views here.

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'Index'
        return render(request, self.template_name, {'variableA': variableA})


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        variableA = 'New Video'
        return render(request, self.template_name, {'variableA': variableA})
