from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from youtube.forms import LoginForm, RegisterForm, NewVideoForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from youtube.models import Video, Comment
import string
import random
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper
from youtube_project.settings import VIDEOS_URL, VIDEOS_NUMBER, COMMENTS_NUMBER


class VideoFileView(View):

    def get(self, request, file_name):
        file = FileWrapper(open(VIDEOS_URL+'/'+file_name, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        return response


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        most_recent_videos = Video.objects.order_by('-datetime')[:VIDEOS_NUMBER]
        return render(request, self.template_name, {'menu_active_item': 'home',
                                                    'most_recent_videos': most_recent_videos})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class VideoView(View):
    template_name = 'video.html'

    def get(self, request, id):
        video_by_id = Video.objects.get(id=id)
        video_by_id.path = VIDEOS_URL + video_by_id.path
        context = {'video': video_by_id}

        if request.user.is_authenticated:
            comment_form = CommentForm()
            context['form'] = comment_form
        comments = Comment.objects.filter(video__id=id).order_by('-datetime')[:COMMENTS_NUMBER]
        context['comments'] = comments
        return render(request, self.template_name, context)


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
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
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')
        return HttpResponse('This is Login view. POST Request.')


class CommentView(View):
    template_name = 'comment.html'

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            video_id = request.POST['video']
            video = Video.objects.get(id=video_id)
            new_comment = Comment(text=text, user=request.user, video=video)
            new_comment.save()
            return redirect(reverse('/video/{}', args=(video_id, )))
        return HttpResponseRedirect('/login')


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
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
        return HttpResponse('This is Register view. POST Request.')


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/login')

        form = NewVideoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NewVideoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']
            random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            path = random_char + file.name
            fs = FileSystemStorage(location=VIDEOS_URL)
            filename = fs.save(path, file)
            fs.url(filename)
            new_video = Video(title=title,
                              description=description,
                              user=request.user,
                              path=path)
            new_video.save()
            return HttpResponseRedirect('/video/{}'.format(new_video.id))
        else:
            return HttpResponse('Form is not valid. Try again.')
