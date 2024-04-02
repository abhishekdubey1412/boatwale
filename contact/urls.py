from django.urls import path
from . import views

urlpatterns = [
    path('contact-us/', views.contact, name="contact"),
]
