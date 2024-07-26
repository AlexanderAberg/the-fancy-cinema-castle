from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Book
from .forms import BookForm

# Create your views here.
class Bookings(generic.ListView):
    queryset = Book.objects.all()
    template_name = 'bookings/bookingmanager.html'