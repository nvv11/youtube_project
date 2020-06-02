from django.shortcuts import render
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from youtube.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'Index'
        return render(request, self.template_name, {'variableA': variableA})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print(request)
        return HttpResponse('This is Login view. POST Request')


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect('/login')
        return HttpResponse('This is Register view. POST Request')


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        variableA = 'New Video'
        return render(request, self.template_name, {'variableA': variableA})
