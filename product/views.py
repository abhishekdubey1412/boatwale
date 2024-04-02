from django.shortcuts import render, get_object_or_404
from .models import Boat, Tour

# Create your views here.
def boat_tours(request):
    boat = Boat.objects.all()
    context = {
        'title': "Varanasi Boat Tours by Boatwale - Explore the Ganges River",
        'description': 'Discover our diverse range of boat tours in Varanasi, from sunrise/sunset cruises to special religious ceremonies, and experience the Ganges River like never before with Boatwale.',
        'keywords': "Varanasi boat tours, Ganges River boat rides, sunrise cruises, sunset cruises, religious ceremonies, Boatwale boat tours, boat experiences",
        'products': boat
    }

    return render(request, 'boat-tour.html', context=context)

def boat_packages(request, slug):
    boat_tour = get_object_or_404(Boat, slug=slug)
    boat_packages = Tour.objects.filter(boat=boat_tour)

    context = {
        'title': boat_tour.name,
        'description': 'Discover our diverse range of boat tours in Varanasi, from sunrise/sunset cruises to special religious ceremonies, and experience the Ganges River like never before with Boatwale.',
        'keywords': "Varanasi boat tours, Ganges River boat rides, sunrise cruises, sunset cruises, religious ceremonies, Boatwale boat tours, boat experiences",
        'boat_tour': boat_tour,
        'boat_packages': boat_packages
    }

    return render(request, 'boat-packages.html', context=context)