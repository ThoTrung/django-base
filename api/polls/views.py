from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from polls.models import Album, Track
# from polls.serializers import TrackSerializer, AlbumSerializer



def index(request):
    albums = Album.objects.all().prefetch_related('tracks') #track_set: default related_name
    for album in albums:
        for track in album.tracks.all():
            print(track.title)

    return HttpResponse('alb')
