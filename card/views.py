from django.shortcuts import render, get_object_or_404
from product.models import Tour, TourImage
import razorpay
from django.conf import settings

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

    if request.method == 'POST':
        name = request.POST.get('name')
        contact_no = request.POST.get('number')
        email = request.POST.get('email')
        age = request.POST.get('age')
        city = request.POST.get('city')
        country = request.POST.get('country')
        time_slot = request.POST.get('pickup_time')
        pickup_ghat = request.POST.get('pickup_ghat')
        date = request.POST.get('pickup_date')
        route = request.POST.get('route')
        person = request.POST.get('person')
        amount = boat_product.new_price * int(person)
        
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
        payment_data = {
            'amount': int(amount * 100),  # Amount in paise
            'currency': 'INR',
            'receipt': 'receipt#1',
            'payment_capture': 1,  # Auto capture
            'notes': {
                'name': name,
                'contact_no': contact_no,
                'email': email,
                'age': age,
                'city': city,
                'country': country,
                'time_slot': time_slot,
                'pickup_ghat': pickup_ghat,
                'date': date,
                'route': route,
                'person': person
            }
        }
        
        payment = client.order.create(data=payment_data)
        return render(request, 'checkout.html', {'payment': payment, 'boat_product': boat_product, 'amount': amount})

    context = {
        'title': "Booking Cart | Boatwale",
        'description': "Explore and review your selected boat tours and experiences in Varanasi with Boatwale's Booking Cart. Ensure your preferred boat rides, cruises, and activities are reserved before proceeding to checkout for a seamless booking process.",
        'keywords': "Boatwale cart, boat tour bookings, Ganges River boat rides, boat tour reservations, boatwale booking system, Varanasi boat tour cart, boatwale checkout",
        'boat_product': boat_product,
        'product_images': product_images
    }

    return render(request, 'booking.html', context=context)