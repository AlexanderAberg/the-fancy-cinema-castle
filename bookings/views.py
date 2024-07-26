from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Book
from .forms import BookForm

# Create your views here.
class Bookings(generic.ListView):
    queryset = Book.objects.all()
    template_name = 'bookings/bookingmanager.html'


def bookings(request):
    if request.method == "POST":
        book_form = BookForm(data=request.POST)
        if book_form.is_valid():
            book_form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for booking an auditorium, we will see you soon.")

    bookings = Bookings.objects.all().order_by('-updated_on').first()
    book_form = BookForm()

    return render(
        request,
        b'ookings/bookingmanager.html',
        {
            'bookings': bookings,
            'book_form': book_form
        },
    )