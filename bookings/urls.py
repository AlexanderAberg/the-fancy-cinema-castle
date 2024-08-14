from django.urls import path
from . import views


urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('book_edit/<int:book_id>/', views.book_edit, name='book_edit'),
    path('delete_book/<int:book_id>/', views.book_delete, name='book_delete'),
]
