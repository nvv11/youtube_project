from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    email = forms.CharField(label='Email', max_length=20)


class CommentForm(forms.Form):
    text = forms.CharField(label='Comment', max_length=300)


class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    description = forms.CharField(label='Description', max_length=300)
    file = forms.FileField()
