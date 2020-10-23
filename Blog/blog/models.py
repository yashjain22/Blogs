from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'author')
    title = models.CharField(max_length = 255, unique=True)
    title_tag = models.CharField(max_length = 255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title