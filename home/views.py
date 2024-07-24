from django.shortcuts import render
from django.views import Home

# Create your views here.

class Home(generic.ListView):
    queryset = Book.objects.all()
    template_name = 'home/index.html'