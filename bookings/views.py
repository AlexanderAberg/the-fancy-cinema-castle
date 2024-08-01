from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book
#from .models import Options
from .forms import BookForm
from cloudinary.models import CloudinaryField

# Create your views here.
class Bookings(generic.ListView):
    queryset = Book.objects.all()
    template_name = 'bookings/bookingmanager.html'


def bookings(request):
    """
Renders the form in the Booking Manager.
    """
    bookings = Book.objects.filter(booker=request.user)

    if request.method == "POST":
        book_form = BookForm(data=request.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.booker = request.user
            book_form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for booking an auditorium, we will see you soon.")

   
    book_form = BookForm()

    return render(
        request,
        'bookings/bookingmanager.html',
        {
            'bookings': bookings,
            'book_form': book_form
        },
    )


def book_edit(request, slug, book_id):
    """
    Display an individual booking for edit.

    **Context**

    ``booking``
        An instance of :model:`booking.Book`.
    ``book``
        A single book related to the booking manager.
    ``book_form``
        An instance of :form:`bookings.BookForm`
    """
    if request.method == "POST":

        book = get_object_or_404(Book, pk=book_id)
        book_form = BookForm(data=request.POST, instance=book)

        if book.booker == request.user:
            book = book_form.save(commit=False)
            book.approved = False
            book.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating booking!')

    return HttpResponseRedirect(reverse('bookingmanager', args=[slug]))




def book_delete(request, slug, book_id):
    """
    Delete an individual booking.

    **Context**

    ``booking``
        An instance of :model:`book.Book`.
    ``book``
        A single book related to the booking manager.
    """

    book = get_object_or_404(Book, pk=book_id)

    if book.booker == request.user:
        book.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'Error with deleting booking')

    return HttpResponseRedirect(reverse('bookingmanager', args=[slug]))