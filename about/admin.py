from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin



class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
# Register your models here.
