from .models import Categories, Posts, Site
from django.urls import reverse


def category(request):
    categories = Categories.objects.all()

    return {
        'categories': categories
    }


def latest_post(request):
    latest_post_01 = Posts.objects.order_by('-date_created')[0:1]
    latest_post_02 = Posts.objects.order_by('-date_created')[1:2]
    latest_post_03 = Posts.objects.order_by('-date_created')[2:3]

    return {
        'latest_post_01': latest_post_01,
        'latest_post_02': latest_post_02,
        'latest_post_03': latest_post_03

    }


def site_settings(request):
    sitename = Site.objects.get(pk=1)
    homepage_url = reverse('index')

    return {
        'site_setting': sitename,
        'homepage': homepage_url
    }
