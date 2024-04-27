from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registration/', views.Registration, name='registration'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('deleteuser/<int:pk>/', views.deleteuser, name='deleteuser'),
    path('autocomplete/', views.ProductAutocompleteView.as_view(), name='product-autocomplete'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name="contact"),
    path('profile/', views.profile, name='profile'),
    path('privacy-policy/', views.policy, name='policy'),
]