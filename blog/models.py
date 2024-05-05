from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

class Post(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=220, null=True, blank=True)
    slug = models.SlugField(unique=True, null=False)
    featured_image = models.ImageField(upload_to='Post Featured Image/', null=True, blank=True)
    featured_alt = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    content = RichTextUploadingField(null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=80, null=False, default=None)
    email = models.EmailField(null=False, default=None)
    body = models.TextField(null=False, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'