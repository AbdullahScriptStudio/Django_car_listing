from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing101
from .utils import get_listings_directory
# Create your views here.


def landing_page(request):
    return HttpResponse('<h1>Welcome to the mars</h1>')


@login_required
def home_page(request):
    return render(request, "views\home.html", {'logged_in': request.user.is_authenticated})

@login_required
def listing_view(request):
    listings = Listing101.objects.all()
    return render(request, 'views\listings.html', {'logged_in': request.user.is_authenticated, 'listings':listings, 'image_url':get_listings_directory })