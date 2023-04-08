from django.db import models


# Create your models here.
class Author(models.Model):
    roles = (
        (1, 'Admin'),
        (2, 'Author'),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    role = models.IntegerField(choices=roles, default=3)
    profile_picture = models.ImageField(upload_to='profiles-pictures/')

    def __str__(self):
        return self.name


