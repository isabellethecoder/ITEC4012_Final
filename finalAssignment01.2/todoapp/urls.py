# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_tv_shows, name='search_tv_shows'),
    path('api/search-tv-shows/', views.search_tv_shows, name='search_tv_shows_api'),
    path('search/', views.search_results, name='search_results'),
    path('show/<int:show_id>/', views.show_index, name='show_index'),  # Add this line
]
