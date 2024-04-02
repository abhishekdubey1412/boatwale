from django.shortcuts import render, get_object_or_404
from product.models import Tour, TourImage

# Create your views here.
def product(request, slug):
    boat_product = get_object_or_404(Tour, slug=slug)
    product_images = TourImage.objects.filter(tour=boat_product)

    context = {
        'title': "Booking Cart - Review Your Selected Boat Tours | Boatwale",
        'description': "Explore and review your selected boat tours and experiences in Varanasi with Boatwale's Booking Cart. Ensure your preferred boat rides, cruises, and activities are reserved before proceeding to checkout for a seamless booking process.",
        'keywords': "Boatwale cart, boat tour bookings, Ganges River boat rides, boat tour reservations, boatwale booking system, Varanasi boat tour cart, boatwale checkout",
        'boat_product': boat_product,
        'product_images': product_images
    }

    return render(request, 'product.html', context=context)

def booking(request, slug):
    boat_product = get_object_or_404(Tour, slug=slug)
    product_images = TourImage.objects.filter(tour=boat_product)

    context = {
        'title': "Booking Cart | Boatwale",
        'description': "Explore and review your selected boat tours and experiences in Varanasi with Boatwale's Booking Cart. Ensure your preferred boat rides, cruises, and activities are reserved before proceeding to checkout for a seamless booking process.",
        'keywords': "Boatwale cart, boat tour bookings, Ganges River boat rides, boat tour reservations, boatwale booking system, Varanasi boat tour cart, boatwale checkout",
        'boat_product': boat_product,
        'product_images': product_images
    }

    return render(request, 'booking.html', context=context)