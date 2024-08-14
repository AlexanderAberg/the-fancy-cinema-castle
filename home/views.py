from django.shortcuts import render


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
