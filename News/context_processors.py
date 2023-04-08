from .models import Categories


def category(request):
    categories = Categories.objects.all()

    return {
        'categories': categories
    }
