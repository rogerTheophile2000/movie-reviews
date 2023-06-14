from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm



# Create your views here.

def news(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})

def createNews(request):
    if request.method == "GET":
        return render(request, "createNews.html", {'form' : NewsForm()})
    else:
        try:
            form = NewsForm(request.POST)
            form.save()
            return redirect("news")
        except ValueError:
            return render(request, "createNews.html", {'form' : NewsForm(), 'error':'bad data passed in'})
    