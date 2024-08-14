from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('date', )
    search_fields = ['user', 'content']
    list_filter = ('date',)
    summernote_fields = ('content',)
