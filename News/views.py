from django.shortcuts import render
from .models import Posts, Categories
from django.views.generic.detail import DetailView
from .models import Posts
from django.shortcuts import get_object_or_404
from django.views import View


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'News/index.html')


class NewsDetailView(DetailView):
    model = Posts
    template_name = 'News/news-details.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Posts, slug=self.kwargs['slug'])
        return obj


def category(request, slug):
    category = Categories.objects.get(slug=slug)

    return render(request, 'News/category.html', {
        'category': category
    })
