from django.shortcuts import render
from django.views import About

# Create your views here.
def About(request):
    """
    Renders the About page
    """
    

    return render(
        request,
        "about/about.html",
        {"about": about},
    )