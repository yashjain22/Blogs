from django.shortcuts import render
from .forms import CreateUserForm,BlogForm
from .models import Post
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.utils import timezone
from django.core.serializers import serialize
from .database_manager import fetch_all_posts as fetch_all,fetch_post_by_id as fetch_by_id
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
@api_view(['POST'])
def register_user(request):
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
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message' : '{0} successfully logged in'.format(username)}, status = status.HTTP_200_OK)
    return JsonResponse({'message' : 'Username or password is incorrect'}, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message' : 'Successfully logged out'}, status = status.HTTP_200_OK)
    return JsonResponse({'message' : 'Not valid request'}, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@login_required(login_url = "api/blog/login")
def create_post(request):
    print(request.body)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.created_on = timezone.now()
            instance.updated_on = timezone.now()
            instance.save()
            return JsonResponse({'message' : 'Post successfully created'}, status = status.HTTP_200_OK)
        else:
            print("hellasadadsadadadaddaadda")
    return JsonResponse({'message' : 'Invalid request'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetch_all_posts(request,orderbydate=0):
    if request.method == 'GET':
        try:
            orderbydate = int(request.GET.get("orderbydate"))
        except:
            orderbydate = 0
        order = 'ASC' if orderbydate == 1 else 'DESC' 
        ans = []
        rows = fetch_all(order)
        for p in rows:
            post = {
                'postid':p.id,
                'title':p.title,
                'title_tag':p.title_tag,
                'body':p.body,
                'created_on':p.created_on.strftime(TIME_FORMAT),
                'updated_on':p.updated_on.strftime(TIME_FORMAT),
                'username':p.username
            }
            ans.append(post)
        return JsonResponse(ans,safe = False,status = status.HTTP_200_OK) if len(ans) > 0 else JsonResponse(ans,safe = False,status = status.HTTP_204_NO_CONTENT)
    return JsonResponse({'message' : 'Invalid request'}, status = status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def fetch_post_by_id(request):
    if request.method == 'GET':
        try:
            postid = int(request.GET.get("postid"))
        except:
            postid = 0
        print(postid)
        if postid <= 0:
            return JsonResponse({'message' : 'Invalid request'}, status = status.HTTP_400_BAD_REQUEST)

        ans = []
        rows = fetch_by_id(postid)
        for p in rows:
            post = {
                'postid':p.id,
                'title':p.title,
                'title_tag':p.title_tag,
                'body':p.body,
                'created_on':p.created_on.strftime(TIME_FORMAT),
                'updated_on':p.updated_on.strftime(TIME_FORMAT),
                'username':p.username,
                'authorid':p.author_id,
                'email':p.email
            }
        ans.append(post)
        return JsonResponse(ans,safe = False,status = status.HTTP_200_OK) if len(ans) > 0 else JsonResponse({},safe = False, status = status.HTTP_204_NO_CONTENT)
    return JsonResponse({'message' : 'Invalid request'}, status = status.HTTP_400_BAD_REQUEST)
