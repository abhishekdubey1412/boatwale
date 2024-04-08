from django.contrib import admin
from .models import Category, Tag, Post, Comment
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_date')
    list_filter = ('published_date', 'author', 'categories', 'tags')
    search_fields = ('title', 'description', 'content')

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
        RichTextUploadingField: {'widget': CKEditorUploadingWidget},
    }

    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('published_date', 'updated_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_date', 'active')
