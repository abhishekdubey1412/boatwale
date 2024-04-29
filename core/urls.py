from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('registration/', views.Registration, name='registration'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('deleteuser/<int:pk>/', views.deleteuser, name='deleteuser'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password-reset.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password-reset-sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-form.html'), name="password_reset_confirm"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password-reset-complete.html'), name="password_reset_complete"),
    
    path('autocomplete/', views.ProductAutocompleteView.as_view(), name='product-autocomplete'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name="contact"),
    path('profile/', views.profile, name='profile'),
    path('privacy-policy/', views.policy, name='policy'),
]