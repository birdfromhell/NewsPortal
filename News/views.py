from django.shortcuts import render
from .models import Posts, Categories
from django.views.generic import ListView
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'News/index.html')


def news(request, slug):
    post = Posts.objects.get(slug=slug)

    return HttpResponse("Works")


def category(request, slug):
    category = Categories.objects.get(slug=slug)

    return render(request, 'News/category.html',{
        'category': category
    })
