from django.urls import path
from . import views
from django.conf.urls import handler404


urlpatterns = [
    path('', views.home, name='home'),
]


handler404 = views.custom_404_view