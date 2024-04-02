from django.urls import path
from . import views

urlpatterns = [
    path('boat-tours/', views.boat_tours, name="boat-tours"),
    path('boat-packages/<slug:slug>/', views.boat_packages, name="boat-packages")
]
