from .models import UserProfile
from django.contrib.auth.models import User
from product.models import Boat, Tour
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    boat = Tour.objects.all()
    products = Boat.objects.all()
    context = {
        'title': "Boatwale - Explore Varanasi Boat Tours on the Ganges River",
        'description': 'Welcome to Boatwale, your trusted platform for discovering unique and memorable boat tours in Varanasi on the sacred Ganges River.',
        'keywords': "Varanasi boat tours, Ganges River experiences, Boatwale, boat rides, boat cruises, Varanasi travel, Ganges River tours",
        'categories': boat,
        'products': products   
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
                return redirect('dashboard')
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