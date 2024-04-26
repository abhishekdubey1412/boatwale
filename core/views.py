from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.models import User
from product.models import Boat, Tour, Route, City
from blog.models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.views import View
import json

# Create your views here.
class ProductAutocompleteView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('term', '')
        Cities = City.objects.filter(city_name__icontains=query)[:10]
        results = [city.city_name for city in Cities]
        return JsonResponse(results, safe=False)

def home(request):
    boat = Tour.objects.all()
    products = Boat.objects.all()
    routes = Route.objects.all()
    seven_days_ago = timezone.now() - timedelta(days=7)
    recent_posts = Post.objects.filter(published_date__gte=seven_days_ago)
    context = {
        'title': "Boatwale - Explore Varanasi Boat Tours on the Ganges River",
        'description': 'Welcome to Boatwale, your trusted platform for discovering unique and memorable boat tours in Varanasi on the sacred Ganges River.',
        'keywords': "Varanasi boat tours, Ganges River experiences, Boatwale, boat rides, boat cruises, Varanasi travel, Ganges River tours",
        'thumbnail': "../static/images/background.png/",
        'categories': boat,
        'products': products,
        'recent_posts': recent_posts,
        'routes': routes
    }
    return render(request, 'home.html', context=context)

def Registration(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            # Retrieve data from the registration form
            username = request.POST.get('registerUsername')
            email = request.POST.get('registerEmail')
            password = request.POST.get('registerPassword')
            confirm_password = request.POST.get('confirmPassword')

            # Validate form data (e.g., check if passwords match, username is unique, etc.)
            if password != confirm_password:
                return render(request, 'registration.html', {'error': 'Passwords do not match'})

            if User.objects.filter(username=username).exists():
                return render(request, 'registration.html', {'error': 'Username already exists'})

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Save user data to UserProfile model
            UserProfile.objects.create(user=user)

            # Optionally, authenticate and login the user immediately after registration
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful registration

        return render(request, 'registration.html')
    else:
        return redirect('home')

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('loginUsername')
            password = request.POST.get('loginPassword')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password'})

        return render(request, 'login.html')
    else:
        return redirect('home')

@login_required(login_url='userlogin')
def userlogout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='userlogin')
def deleteuser(request, pk):
    delete_user = User.objects.get(id=pk)
    delete_user.delete()
    return redirect('dashboard')


def about(request):
    context = {
        'title': 'About Boatwale - Your Varanasi Boat Tour Specialist',
        'description': 'Learn more about Boatwale, our dedication to offering exceptional boat tours, and our passion for showcasing the beauty and heritage of Varanasi.',
        'keywords': "Boatwale, Varanasi boat tours, boat tour specialist, Ganges River experiences, boat tour providers, Varanasi travel, boat tour company"
    }
    
    return render(request, 'about.html', context=context)


# Create your views here.
def contact(request):
    context = {
        'title': "Contact Boatwale - Get in Touch for Varanasi Boat Tours",
        'description': "Have questions or need assistance? Reach out to the Boatwale team, and we'll be happy to help you plan your perfect boat tour experience in Varanasi.",
        'keywords': "Boatwale contact, Varanasi boat tours inquiry, Ganges River boat rides, boat tour booking, customer support, boatwale assistance, Varanasi travel planning"
    }

    if request.method == "POST":
        # Retrieve form data
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Create a new Contact instance and save it to the database
        contact_entry = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )
        contact_entry.save()

        # Add a success message
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'contact.html', context=context)


@login_required(login_url='userlogin')
def profile(request):
    xArray = ["Italy", "France", "Spain", "USA", "Argentina"]
    yArray = [55, 49, 44, 24, 15]
    barColors = ["red", "green","blue","orange","brown"]
    user_pk = request.user.pk

    context = {
        'title': 'My Account - Manage Your Boatwale User Profile | Boatwale',
        'description': "Access and manage your Boatwale user account with ease. View your booking history, update account settings, save favorite boat tours, and more in your personalized profile to enhance your Varanasi boat tour experience with Boatwale.",
        'keywords': "Boatwale profile, user account, boat tour history, Ganges River experiences, boatwale user profile, Varanasi travel profile, boatwale account settings",
        'xArray': json.dumps(xArray),
        'yArray': json.dumps(yArray),
        'barColors': barColors,
        'user_pk': user_pk,
    }

    return render(request, 'profile.html', context=context)