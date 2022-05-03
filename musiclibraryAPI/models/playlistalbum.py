from django.db import models


class PlaylistAlbum(models.Model):

    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)
