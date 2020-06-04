from django.shortcuts import render
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from youtube.forms import LoginForm, RegisterForm, NewVideoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'Index'
        return render(request, self.template_name, {'menu_active_item': 'home'})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('Already Logged In. Redirecting')
            print(request.user)
            return HttpResponseRedirect('/')
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('Successful Login')
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')
        return HttpResponse('This is Login view. POST Request')


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('Already Logged In. Redirecting')
            print(request.user)
            return HttpResponseRedirect('/')
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
        form = NewVideoForm()
        return render(request, self.template_name, {'variableA': variableA, 'form': form})

    def post(self, request):
        return HttpResponse('This is Index view. POST Request.')
