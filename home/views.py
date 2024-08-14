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

def custom_404_view(request, exception):
    return render(request, '404.html', {}, status=404)