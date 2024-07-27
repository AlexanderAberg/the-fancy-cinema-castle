from django.shortcuts import render
from cloudinary.models import CloudinaryField

# Create your views here.
def about(request):
    """
    Renders the About page
    """
    

    return render(
        request,
        "about/about.html",
        {"about": about},
    )