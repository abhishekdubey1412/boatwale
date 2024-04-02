from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required

@login_required(login_url='userlogin')
def dashboard(request):
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

    return render(request, 'dashboard/dashboard.html', context=context)


def main_dashboard(request):
    return render(request, 'main-dashboard/pages/dashboard.html')

def main_tables(request):
    return render(request, 'main-dashboard/pages/tables.html')

def main_billing(request):
    return render(request, 'main-dashboard/pages/billing.html')

def main_profile(request):
    return render(request, 'main-dashboard/pages/profile.html')

def main_vr(request):
    return render(request, 'main-dashboard/pages/virtual-reality.html')

def main_profile(request):
    return render(request, 'main-dashboard/pages/profile.html')

def main_sing_in(request):
    return render(request, 'main-dashboard/pages/sign-in.html')

def main_sing_up(request):
    return render(request, 'main-dashboard/pages/sign-up.html')