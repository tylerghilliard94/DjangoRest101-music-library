from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
