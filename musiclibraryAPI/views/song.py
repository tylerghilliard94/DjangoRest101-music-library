"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from musiclibraryAPI.models import Song
from musiclibraryAPI.models.album import Album
from musiclibraryAPI.views.album import AlbumSerializer


class SongView(ViewSet):
    """Music Library Song view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single song

        Returns:
            Response -- JSON serialized song
        """
        song = Song.objects.get(pk=pk)

        serializer = SongSerializer(song)

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all songs

        Returns:
            Response -- JSON serialized list of songs
        """

        songs = Song.objects.all()

        serializer = SongSerializer(songs, many=True)

        return Response(serializer.data)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField(source='pk', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class SongSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    album = AlbumSerializer()

    class Meta:
        model = Song
        fields = ('id', 'song_title', 'artist', 'album', 'user')
        depth = 1
