from django.shortcuts import render
from .models import Posts


# Create your views here.
def index(request):
    return render(request, 'News/index.html')


def category(request):
    return render(request, 'News/category.html')
