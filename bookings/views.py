from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import Book
from .forms import BookForm


# Create your views here.
class Bookings(generic.ListView):
    queryset = Book.objects.all()
    template_name = 'bookings/bookingmanager.html'


# The Booking view
def bookings(request):
    """
    Renders the form in the Booking Manager.
    """
    bookings = Book.objects.filter(booker=request.user.id)
    session_type_choices = Book._meta.get_field('session_type').choices
    options_choices = Book._meta.get_field('options').choices

    if request.method == "POST":
        book_form = BookForm(data=request.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.booker = request.user
            book.save()
            messages.add_message
            (request, messages.SUCCESS,
             "Thank you for booking an auditorium, we will see you soon.")
            return HttpResponseRedirect(reverse('bookings'))
    else:
        book_form = BookForm()

    return render(
        request,
        'bookings/bookingmanager.html',
        {
            'bookings': bookings,
            'session_type_choices': session_type_choices,
            'options_choices': options_choices,
            'book_form': book_form,
        }
    )


# The Edit Booking view
def book_edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book_form = BookForm(request.POST, instance=book)
        if book_form.is_valid():
            book_form.save()
            messages.success(request, 'Booking updated successfully!')
            return JsonResponse({'status': 'success'}, status=200)
        else:
            messages.error(request, 'There was an error updating the booking.')
            return JsonResponse({'status': 'error', 'errors':
                                 book_form.errors}, status=400)
    if request.method == "GET":
        data = {
            'session_type': book.session_type,
            'amount': book.amount,
            'options': book.options,
            'wishes': book.wishes,

        }
        return JsonResponse(data)
    return JsonResponse({'status': 'error'}, status=400)


# The Delete Booking view
def book_delete(request, book_id):

    book = get_object_or_404(Book, pk=book_id)

    if book.booker == request.user:
        book.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'Error with deleting booking')

    return HttpResponseRedirect(reverse('bookings'))
