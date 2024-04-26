from django.shortcuts import render

def dashboard(request):

    context = {
        'title': 'My Account - Manage Your Boatwale User Profile | Boatwale',
        'description': "Access and manage your Boatwale user account with ease. View your booking history, update account settings, save favorite boat tours, and more in your personalized profile to enhance your Varanasi boat tour experience with Boatwale.",
        'keywords': "Boatwale profile, user account, boat tour history, Ganges River experiences, boatwale user profile, Varanasi travel profile, boatwale account settings",
    }

    return render(request, 'admin/dashboard.html', context=context)