from django.contrib import admin
from .models import Book
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('date',)
    search_fields = ['user']
    list_filter = ('date',)
    summernote_fields = ('content',)

# Register your models here.
