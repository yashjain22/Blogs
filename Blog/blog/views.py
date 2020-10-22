from django.shortcuts import render
from .forms import CreateUserForm,BlogForm
# Create your views here.
#from rest_framework import viewsets


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
 
#from tutorials.models import Tutorial
#from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
from django.utils import timezone

@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        print(request)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            form.save()
            return JsonResponse({'message' : 'User Successfully Registered'},status = status.HTTP_200_OK)
    print(form.errors)
    return JsonResponse({'message' : 'Not valid request'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message' : '{0} successfully logged in'.format(username)}, status = status.HTTP_200_OK)
    return JsonResponse({'message' : 'Username or password is incorrect'}, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message' : 'Successfully logged out'}, status = status.HTTP_200_OK)
    return JsonResponse({'message' : 'Not valid request'}, status = status.HTTP_400_BAD_REQUEST)


@login_required(login_url = "api/blog/login")
def createPost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            instance = form.commit(False)
            instance.author = request.user
            instance.created_on = timezone.now()
            instance.updated_on = timezone.now()
            instance.save()
            print("post saved")
            return JsonResponse({'message' : 'Post successfully created'}, status = status.HTTP_200_OK)
    return JsonResponse({'message' : 'Invalid request'}, status = status.HTTP_400_BAD_REQUEST)



