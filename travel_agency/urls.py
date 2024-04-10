from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('contact.urls')),
    path('', include('card.urls')),
    path('', include('product.urls')),
    path('', include('blog.urls')),
    path('', include('about.urls')),
    path('', include('dashboard.urls')),
     path('', RedirectView.as_view(url='http://www.boatwale.com/', permanent=True)),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)