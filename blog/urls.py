from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name="blog"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('tag/<slug:slug>/', views.TagDetailView.as_view(), name='tag_detail'),
]
