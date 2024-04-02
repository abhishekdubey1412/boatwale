from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    content = models.TextField(null=False, default='')
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, default=None)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=80, null=False, default=None)
    email = models.EmailField(null=False, default=None)
    body = models.TextField(null=False, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)