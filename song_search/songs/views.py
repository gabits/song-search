from django.shortcuts import render
from models import Songs
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


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
    songs_list = Songs.objects.all().order_by('artist', 'song_name')
    pagination = Paginator(songs_list, 25)
    num_current_page = request.GET.get('page')
    try:
        page = pagination.page(num_current_page)
    except PageNotAnInteger:
        page = pagination.page(1)
    except EmptyPage:
        page = pagination.page(pagination.num_pages)
    all_page_songs = []
    for row in page.object_list:
        if len(row.lyrics) <= 100:
            lyrics_preview = row.lyrics
        else:
            lyrics_preview = str(row.lyrics[:100]) + '...'
        song_dict = {
            'artist': row.artist,
            'song_name': row.song_name,
            'lyrics': lyrics_preview,
            'id': row.id,
        }
        all_page_songs.append(song_dict)

    # Navigation through pages
    if page.number - 1 < 1:
        prev_page = 1
    else:
        prev_page = page.previous_page_number()
    if page.number + 1 > pagination.num_pages:
        next_page = pagination.num_pages
    else:
        next_page = page.next_page_number()
    if page.number - 10 < 1:
        previous_10 = 1
    else:
        previous_10 = page.number - 10
    if page.number - 100 < 1:
        previous_100 = 1
    else:
        previous_100 = page.number - 100
    if page.number + 10 < 1:
        next_10 = 1
    else:
        next_10 = page.number + 10
    if page.number + 100 < 1:
        next_100 = 1
    else:
        next_100 = page.number + 100

    context = {
        'page_songs': all_page_songs,
        'page': page,
        'prev_page': prev_page,
        'next_page': next_page,
        'previous_10': previous_10,
        'previous_100': previous_100,
        'next_10': next_10,
        'next_100': next_100,
        'last_page': pagination.num_pages,
    }
    return render(request, 'manage.html', context)


def details(request):
    id = request.GET['id']
    song_info = Songs.objects.get(pk=id)
    context = {'artist': song_info.artist,
               'song_name': song_info.song_name,
               'lyrics': song_info.lyrics
               }
    return render(request, 'details.html', context)
