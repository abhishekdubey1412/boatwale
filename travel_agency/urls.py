from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, CategorySitemap, TagSitemap, BoatSitemap, TourSitemap, StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'posts': PostSitemap,
    'categories': CategorySitemap,
    'tags': TagSitemap,
    'boats': BoatSitemap,
    'tours': TourSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('card.urls')),
    path('', include('product.urls')),
    path('', include('blog.urls')),
    path('', include('core.urls')),
    path('', include('dashboard.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    # path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)