from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<slug:slug>', views.news, name="news"),
    path('category/<slug:slug>', views.category, name='category')
]