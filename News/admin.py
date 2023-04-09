from django.contrib import admin
from .models import Posts, Categories, Tags, Site
# Register your models here.


admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Site)
