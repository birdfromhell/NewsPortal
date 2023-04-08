from django.db import models
from users.models import Author
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', args=(self.slug,))

    def number_of_categories(self):
        count = Posts.objects.filter(category=self.id).count()

        return count


class Posts(models.Model):
    status_choice = ((1, 'Draft'),
                     (2, 'Published'),
                     (3, 'Archived'),
                     (4, 'Schedule'))

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='postimage/', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField("Tags", blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    featured = models.BooleanField(default=False)
    breaking_news = models.BooleanField(null=True)
    status = models.IntegerField(choices=status_choice)
    page_views = models.IntegerField(default=0, editable=False)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news', args=(self.slug,))


class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
