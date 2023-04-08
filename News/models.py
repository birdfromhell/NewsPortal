from django.db import models
from users.models import Author
from django.utils.text import slugify


# Create your models here.
class Posts(models.Model):
    status_choice = ((1, 'Draft'),
                     (2, 'Published'),
                     (3, 'Archived'),
                     (4, 'Schedule'))

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='postimage/', blank=True)
    author = models.ManyToManyField(Author, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tags", blank=True)
    category = models.ManyToManyField("Categories", blank=True)
    featured = models.BooleanField(default=False)
    breaking_news = models.BooleanField(default=False)
    status = models.IntegerField(choices=status_choice)
    page_views = models.IntegerField(default=0, editable=False)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)


class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
