from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)


def details(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    # try:
    #     album = Album.objects.get(id=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")
    return render(request, 'music/details.html', {'album': album})


def favourite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {
            'error_message': 'Please select a valid option',
            'album': album
        })
    if selected_song.is_favourite is False:
        selected_song.is_favourite = True
        selected_song.save()
    return render(request, 'music/details.html', {'album': album})


def downloads(request):
    return HttpResponse("<h1>This is the Music Download Page</h1>")
