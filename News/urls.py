from django.urls import path
from. import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('news/<slug:slug>', views.NewsDetailView.as_view(), name="news"),
    path('category/<slug:slug>', views.category, name='category')
]