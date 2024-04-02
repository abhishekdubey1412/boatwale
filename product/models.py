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

    def save(self, *args, **kwargs):
        super(Boat, self).save(*args, **kwargs)
        
        if self.image:
            webp_image_path = self.convert_image_to_webp()

            # Update the image field with the new WebP image
            self.image = f'boats/{os.path.basename(webp_image_path)}'

            # Save the updated image field
            super(Boat, self).save(*args, **kwargs)

    def convert_image_to_webp(self):
        img = Image.open(self.image.path)

        # Convert image to WebP format
        webp_image_path = os.path.splitext(self.image.path)[0] + '.webp'
        img.save(webp_image_path, 'WEBP', quality=85)

        # Remove the original image file
        os.remove(self.image.path)

        return webp_image_path


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
    
    def save(self, *args, **kwargs):
        # Check if the image format is already WEBP
        if self.image and os.path.splitext(self.image.name)[1].lower() != '.webp':
            super(Tour, self).save(*args, **kwargs)
            webp_image_path = self.convert_image_to_webp()

            # Update the image field with the new WebP image
            self.image = f'tours/{os.path.basename(webp_image_path)}'

            # Save the updated image field
            super(Tour, self).save(*args, **kwargs)
        else:
            super(Tour, self).save(*args, **kwargs)

    def convert_image_to_webp(self):
        img = Image.open(self.image.path)

        # Convert image to WebP format
        webp_image_path = os.path.splitext(self.image.path)[0] + '.webp'
        img.save(webp_image_path, 'WEBP', quality=85)

        # Remove the original image file
        os.remove(self.image.path)

        return webp_image_path
    
    
class TourImage(models.Model):
    image = models.ImageField(upload_to='tours-packages/', null=True, blank=True)
    alt = models.CharField(max_length=100, null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)

    def save(self, *args, **kwargs):
        # Check if the image format is already WEBP
        if self.image and os.path.splitext(self.image.name)[1].lower() != '.webp':
            super(TourImage, self).save(*args, **kwargs)
            webp_image_path = self.convert_image_to_webp()

            # Update the image field with the new WebP image
            self.image = f'tours-packages/{os.path.basename(webp_image_path)}'

            # Save the updated image field
            super(TourImage, self).save(*args, **kwargs)
        else:
            super(TourImage, self).save(*args, **kwargs)
            self.resize_and_save_image()
            super(TourImage, self).save(*args, **kwargs)

    def resize_and_save_image(self):
        img = Image.open(self.image.path)

        # Resize image to 589x441
        img = img.resize((589, 441))

        # Save resized image to the correct directory
        img.save(self.image.path, 'WEBP', quality=85)

    def convert_image_to_webp(self):
        img = Image.open(self.image.path)

        # Resize image to 589x441
        img = img.resize((589, 441))

        # Convert image to WebP format
        webp_image_path = os.path.splitext(self.image.path)[0] + '.webp'
        img.save(webp_image_path, 'WEBP', quality=85)

        # Remove the original image file
        os.remove(self.image.path)

        return webp_image_path

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.tour.name}"