from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {
        'title': "Boatwale Blog - Stories, Tips, and Insights on Varanasi Boating",
        'description': 'Stay updated with the latest stories, tips, and insights about boating in Varanasi on the Boatwale blog, curated for both enthusiasts and travelers.',
        'keywords': "Varanasi boating, boatwale blog, Ganges River stories, boating tips, boat tour insights, Varanasi travel guide, boatwale updates"
    }
    return render(request, 'blog.html', context=context)

def post(request):
    context = {
        'title': "Varanasi: The Spiritual Heart of India"
    }
    return render(request, 'single-blog.html', context=context)