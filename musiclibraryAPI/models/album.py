from django.db import models


class Album(models.Model):

    album_title = models.CharField(max_length=40)
    year_created = models.CharField(max_length=4)
    playlists = models.ManyToManyField(
        'Playlist', through='playlistAlbum', related_name='albums')
