# from polls.models import Album, Track
# from polls.serializers import TrackSerializer, AlbumSerializer

# album = Album.objects.create(album_name="The Grey Album", artist='Danger Mouse')
# Track.objects.create(album=album, order=1, title='Public Service Announcement', duration=245)
# Track.objects.create(album=album, order=2, title='What More Can I Say', duration=264)
# Track.objects.create(album=album, order=3, title='Encore', duration=159)

# album1 = Album.objects.create(album_name="test 1", artist='test1 a')
# Track.objects.create(album=album1, order=4, title='test 2', duration=245)

# albums = Album.objects.all().prefetch_related('tracks')
# tracks = Track.objects.all().prefetch_related('album')


# serializer = AlbumSerializer(albums, many=True)
# serializer.data
