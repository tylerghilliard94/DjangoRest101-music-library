from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):

    song_title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
