from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.








def home(request):
    searchTerm = request.GET.get('searchMovie')
    # search implementation
    if searchTerm:
        movies = Movie.objects.filter(title__icontains = searchTerm)
    else:
        movies = Movie.objects.all().order_by('-title')
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies': movies})


def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

