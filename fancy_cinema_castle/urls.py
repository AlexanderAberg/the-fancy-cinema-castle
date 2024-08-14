#URL for The Fancy Cinema Castle
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from home.views import custom_404_view

urlpatterns = [
    path('about/', include('about.urls'), name='about-urls'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls'), name='bookings-urls'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls'), name='home-urls'),
]


handler404 = custom_404_view