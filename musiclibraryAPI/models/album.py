from django.db import models

class Album(models.Model):

    album_title = models.CharField(max_length=50)
    year_created= models.CharField(max_length=4)
