from django.contrib import sitemaps
from django.urls import reverse
from blog.models import Post, Category, Tag
from product.models import Boat, Tour

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'contact']

    def location(self, item):
        return reverse(item)

class PostSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_date

class CategorySitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return Category.objects.all()

class TagSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Tag.objects.all()

class BoatSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return Boat.objects.all()

class TourSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Tour.objects.all()

    def lastmod(self, obj):
        return obj.update_at