from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def search_songs(request):
    search_text = (request.GET['search_box']).strip()
    search_filter = request.GET.has_key('filter')
    if len(search_text) > 0 and search_filter:
        context = {
            'songs': [{
                'name': 'Dancing Queen',
                'artist': 'ABBA',
                'album': 'ABBA',
                'lyrics': 'You are the dancing queen',
            }
            ]
        }
        return render(request, 'results.html', context)
    elif len(search_text) > 0 and not search_filter:
        context = {
            'error': 'Choose a filter for your search.',
            'search_box': request.GET['search_box'],
        }
        return render(request, 'index.html', context)
    else:
        context = {
            'error': 'Type something for your search.',
        }
        if search_filter:
            context.update({'filter': request.GET['filter']})
            print(context)
        return render(request, 'index.html', context)


def previous(request):
    return render(request, 'index.html')