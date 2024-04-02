from django.shortcuts import render

# Create your views here.
def about(request):
    context = {
        'title': 'About Boatwale - Your Varanasi Boat Tour Specialist',
        'description': 'Learn more about Boatwale, our dedication to offering exceptional boat tours, and our passion for showcasing the beauty and heritage of Varanasi.',
        'keywords': "Boatwale, Varanasi boat tours, boat tour specialist, Ganges River experiences, boat tour providers, Varanasi travel, boat tour company"
    }
    
    return render(request, 'about.html', context=context)