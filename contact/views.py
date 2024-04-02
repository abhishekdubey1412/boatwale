from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

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