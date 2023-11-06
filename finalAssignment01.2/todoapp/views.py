from django.shortcuts import render
from .models import SearchBar, SearchQuery
from django.http import JsonResponse
import requests


def index(request):
    return render(request, 'index.html')


def search_results(request):
    query = request.GET.get('query', '')
    results = SearchBar.objects.filter(search_nav__icontains=query)

    # Save the search query to the database
    if query:
        SearchQuery.objects.create(query=query)

    return render(request, 'index.html', {'results': results, 'query': query})


def search_tv_shows(request):
    query = request.GET.get('query', '')

    if query:
        api_url = f'https://api.tvmaze.com/search/shows?q={query}'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            results = []

            for show_data in data:
                show = show_data.get('show', {})
                result = {
                    'name': show.get('name', ''),
                    'premiered': show.get('premiered', ''),
                    'summary': show.get('summary', '')
                }
                results.append(result)
        else:
            results = []  # Handle API request errors gracefully
    else:
        results = []  # Handle the case where no query is provided

    return render(request, 'index.html', {'results': results, 'query': query})