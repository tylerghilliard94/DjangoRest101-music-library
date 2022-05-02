from django.db import models
from django.contrib.auth.models import User


class Playlist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    albums = models.ManyToManyField("Album")
