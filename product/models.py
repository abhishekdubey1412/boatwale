from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Boat(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    capacity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='boats/')

    def __str__(self):
        return self.name
    
class Tour(models.Model):
    image = models.ImageField(upload_to='tours/', null=True, blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField()
    duration = models.IntegerField()
    old_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    new_price = models.DecimalField(max_digits=8, decimal_places=2)
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    available_seats = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class TourImage(models.Model):
    image = models.ImageField(upload_to='tours-packages/', null=True, blank=True)
    alt = models.CharField(max_length=100, null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    time_slot = models.TimeField(max_length=50)
    pickup_ghat = models.CharField(max_length=100)
    date = models.DateField()
    route = models.CharField(max_length=200)
    total_guests = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_id = models.CharField(max_length=50)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.tour.name}"