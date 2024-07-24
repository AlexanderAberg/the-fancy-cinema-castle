from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin



class HomeAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
# Register your models here.
