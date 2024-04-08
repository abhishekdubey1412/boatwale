from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name="blog"),
    path('post/<slug:slug>/', views.post, name="post")
]
