from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book
#from .models import Options

# Register your models here.
@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('date', )
    search_fields = ['user', 'content']
    list_filter = ('date',)
    summernote_fields = ('content',)


#admin.site.register(Options)
