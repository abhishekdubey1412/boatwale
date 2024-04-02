from django.urls import path
from . import views

urlpatterns = [
    path('product/<slug:slug>/', views.product, name="product"),
    path('booking/<slug:slug>/', views.booking, name="booking")
]
