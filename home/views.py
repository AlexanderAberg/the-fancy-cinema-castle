from django.shortcuts import render
from cloudinary.models import CloudinaryField

# Create your views here.
def home(request):
    """
    Renders the Home page
    """
    

    return render(
        request,
        "home/index.html",
        {"home": home},
    )