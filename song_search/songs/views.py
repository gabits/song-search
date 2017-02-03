from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import Songs


def index(request):
    return render(request, 'index.html')


def search_songs(request):
    search_text = (request.GET['search_box']).strip()
    has_search_filter = request.GET.has_key('filter')
    if len(search_text) > 0 and has_search_filter:
        results_list = []
        selected_filter = request.GET['filter']
        if selected_filter == 'artist':
            filt = Songs.objects.filter(artist__icontains=search_text)
        elif selected_filter == 'song_name':
            filt = Songs.objects.filter(song_name__icontains=search_text)
        else:
            filt = Songs.objects.filter(lyrics__icontains=search_text)
        for row in filt.order_by('artist', 'song_name'):
            if len(row.lyrics) <= 100:
                lyrics_preview = row.lyrics
            else:
                lyrics_preview = str(row.lyrics[:100]) + '...'
            song_data = {
                'artist': row.artist,
                'song_name': row.song_name,
                'lyrics': lyrics_preview,
                'id': row.id,
            }
            results_list.append(song_data)
        context = {
            'result': results_list
        }
        return render(request, 'results.html', context)
    elif len(search_text) > 0 and not has_search_filter:
        context = {
            'error': 'Choose a filter for your search.',
            'search_box': request.GET['search_box'],
        }
        return render(request, 'index.html', context)
    else:
        context = {
            'error': 'Type something for your search.',
        }
        if has_search_filter:
            context.update({'filter': request.GET['filter']})
        return render(request, 'index.html', context)


def previous(request):
    return render(request, 'index.html')


def manage(request):
    return render(request, 'manage.html')


def details(request):
    id = request.GET['id']
    song_info = Songs.objects.get(pk=id)
    context = {'artist': song_info.artist,
               'song_name': song_info.song_name,
               'lyrics': song_info.lyrics
               }
    return render(request, 'details.html', context)