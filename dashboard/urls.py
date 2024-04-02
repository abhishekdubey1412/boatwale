from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('main_dashboard/', views.main_dashboard, name='main_dashboard'),
    path('main_tables/', views.main_tables, name='main_tables'),
    path('main_billing/', views.main_billing, name='main_billing'),
    path('main_vr/', views.main_vr, name='main_vr'),
    path('main_profile/', views.main_profile, name='main_profile'),
    path('main_sing_in/', views.main_sing_in, name='main_sing_in'),
    path('main_sing_up/', views.main_sing_up, name='main_sing_up'),
]
