from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']
        exclude = ['author','created_on','updated_on']