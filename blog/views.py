from django.shortcuts import render, get_object_or_404
from .models import Category, Post

# Create your views here.
def blog(request):
    content_category = Category.objects.all()
    content_posts = Post.objects.all()
    context = {
        'title': "Boatwale Blog - Stories, Tips, and Insights on Varanasi Boating",
        'description': 'Stay updated with the latest stories, tips, and insights about boating in Varanasi on the Boatwale blog, curated for both enthusiasts and travelers.',
        'keywords': "Varanasi boating, boatwale blog, Ganges River stories, boating tips, boat tour insights, Varanasi travel guide, boatwale updates",
        'categories': content_category,
        'posts': content_posts
    }
    return render(request, 'blog.html', context=context)

def post(request, slug):
    post_content = get_object_or_404(Post, slug=slug)
        
    context = {
        'title': post_content.title,
        'description': post_content.description,
        'content': post_content
    }
    
    return render(request, 'single-blog.html', context=context)