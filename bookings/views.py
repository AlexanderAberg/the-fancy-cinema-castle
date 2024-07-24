from django.shortcuts import render
from django.views import Bookings
from .models import Book

# Create your views here.
class Bookings(generic.ListView):
    queryset = Book.objects.all()
    template_name = 'bookings/bookingmanager.html'