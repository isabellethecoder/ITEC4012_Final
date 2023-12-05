# views.py
from django.shortcuts import render
import requests

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
                    'id': show.get('id', ''),  # Added to pass show ID to the show_index view
                    'name': show.get('name', ''),
                }

                # Fetch show images
                images_url = f'https://api.tvmaze.com/shows/{show["id"]}/images'
                images_response = requests.get(images_url)
                if images_response.status_code == 200:
                    images_data = images_response.json()
                    if images_data:
                        # Find the first image with a resolution of 'original'
                        for image_data in images_data:
                            if 'original' in image_data.get('resolutions', {}):
                                result['image'] = image_data['resolutions']['original']['url']
                                break  # Break the loop once the first image is found

                results.append(result)
        else:
            results = []  # Handle API request errors gracefully
    else:
        results = []  # Handle the case where no query is provided

    # Fetch themed shows for the homepage
    themed_shows = get_themed_shows()

    return render(request, 'index.html', {'results': results, 'query': query, 'categories': themed_shows})

def search_results(request):
    # Your view logic for search results
    return render(request, 'search_results.html', context={})

def show_index(request, show_id):
    api_url = f'https://api.tvmaze.com/shows/{show_id}?embed=episodes'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        show_info = {
            'name': data.get('name', ''),
            'premiered': data.get('premiered', ''),
            'summary': data.get('summary', ''),
            'episodes': data.get('_embedded', {}).get('episodes', []),
        }

        # Specify the keywords you want to filter by for each group
        keywords_by_group = {
            'Christmas': ["Christmas", "Holiday"],
            'Halloween': ["Halloween"],
            'Hanukkah': ["Hanukkah"],
            'Thanksgiving': ["Thanksgiving"],
            'Easter': ["Easter"],
            'New Year': ["New Year", "New Year's Eve", "New Year's Day"],
            'Diwali': ["Diwali"],
            'Valentine\'s Day': ["Valentine's Day", "Valentine Day", "Valentines Day"],
            'Independence Day': ["Independence Day"],
            'Labor Day': ["Labor Day"],
            'Cultural Festivals': ["Carnival", "Oktoberfest", "Lunar New Year"],
            'St-Patric\'s Day': ["St-Patric.", "St. Patty", "St. Patric"],
            # Add more holidays as needed
        }

        # Group episodes based on the keywords in the episode summary
        grouped_episodes = {group: [] for group in keywords_by_group}

        for episode in show_info['episodes']:
            title = episode.get('name', '')
            summary = episode.get('summary', '')
            episode_number = episode.get('number', '')
            season_number = episode.get('season', '')

            # Check if summary is not None before converting to lowercase
            if summary is not None:
                for group, keywords in keywords_by_group.items():
                    if any(keyword.lower() in summary.lower() for keyword in keywords):
                        grouped_episodes[group].append({
                            'title': title,
                            'summary': summary,
                            'episode_number': episode_number,
                            'season_number': season_number,
                        })

        # Remove empty groups
        grouped_episodes = {group: episodes for group, episodes in grouped_episodes.items() if episodes}

        return render(request, 'showIndex.html', {'show_info': show_info, 'grouped_episodes': grouped_episodes})
    else:
        # Handle API request errors gracefully
        return render(request, 'error.html')  # Create an error template or redirect as needed

def extract_image_urls(text):
    """Extract image URLs from the given text."""
    # Use a regular expression to find URLs in the text
    import re
    url_pattern = re.compile(r'https?://\S+')
    return url_pattern.findall(text)

def get_themed_shows():
    """Fetch themed shows for the homepage."""
    themed_shows = {
        'Christmas': get_shows_by_keyword("Christmas", 5),
        'Halloween': get_shows_by_keyword("Halloween", 5),
        'Thanksgiving': get_shows_by_keyword("Thanksgiving", 5),
    }
    return themed_shows

def get_shows_by_keyword(keyword, count):
    """Fetch shows based on the given keyword."""
    api_url = f'https://api.tvmaze.com/search/shows?q={keyword}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        shows = []

        for show_data in data[:count]:
            show = show_data.get('show', {})
            result = {
                'id': show.get('id', ''),  # Added to pass show ID to the show_index view
                'name': show.get('name', ''),
            }

            # Fetch show images
            images_url = f'https://api.tvmaze.com/shows/{show["id"]}/images'
            images_response = requests.get(images_url)
            if images_response.status_code == 200:
                images_data = images_response.json()
                if images_data:
                    # Find the first image with a resolution of 'original'
                    for image_data in images_data:
                        if 'original' in image_data.get('resolutions', {}):
                            result['image'] = image_data['resolutions']['original']['url']
                            break  # Break the loop once the first image is found

            shows.append(result)

        return shows
    else:
        return []  # Handle API request errors gracefully
