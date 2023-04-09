from django.shortcuts import render
from ninja import NinjaAPI
from News.models import Posts
from typing import List
from .serializers import NewsSchema
from ninja.pagination import paginate, PageNumberPagination
# Create your views here.
router = NinjaAPI()


@router.get("/posts", response=List[NewsSchema])
@paginate(PageNumberPagination, page_size=2)
def index(request):
    a = Posts.objects.select_related("category")
    return Posts.objects.all()
