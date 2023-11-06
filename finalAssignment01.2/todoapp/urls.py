from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/search-tv-shows/', views.search_tv_shows, name='search_tv_shows'),
]