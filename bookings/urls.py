from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bookings.as_view(), name='bookings'),
    path('<slug:slug>/edit_book/<int:book_id>',
         views.book_edit, name='book_edit'),
    path('<slug:slug>/delete_book/<int:book_id>',
         views.book_delete, name='book_delete'),
]