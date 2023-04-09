from django.db import models
from users.models import Author
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


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


# class Tags(models.Model):
#     name = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name


class Posts(models.Model):
    status_choice = (("draft", 'Draft'),
                     ("published", 'Published'),
                     ("archived", 'Archived'),
                     ("schedule", 'Schedule'))

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='postimage/', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, editable=True)
    content = RichTextField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    status = models.CharField(choices=status_choice, max_length=20)
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


class Site(models.Model):
    sitename = models.CharField(max_length=50)
    site_logo = models.ImageField(upload_to='sitelogo/', blank=True)
    favicon = models.ImageField(upload_to='favicon/', blank=True)
    instagram_link = models.CharField(max_length=50, null=True)
    facebook_link = models.CharField(max_length=50, null=True)
    twitter_link = models.CharField(max_length=50, null=True)
    youtube_link = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.sitename
