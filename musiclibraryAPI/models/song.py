from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):

    song_title = models.CharField(max_length=40)
    artist = models.CharField(max_length=20)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
