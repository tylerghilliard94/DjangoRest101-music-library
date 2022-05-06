"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from musiclibraryAPI.models import Album
from musiclibraryAPI.models.playlist import Playlist
from django.contrib.auth.models import User


class AlbumView(ViewSet):
    """Music Library Album view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single album

        Returns:
            Response -- JSON serialized album
        """

        album = Album.objects.get(pk=pk)

        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all albums

        Returns:
            Response -- JSON serialized list of albums
        """

        albums = Album.objects.all()

        serializer = AlbumSerializer(
            albums, many=True
        )
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateAlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        album = Album.objects.get(pk=serializer.data['id'])
        album.playlists.add(*request.data['playlists'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        album = Album.objects.get(pk=pk)
        serializer = CreateAlbumSerializer(album, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        album = Album.objects.get(pk=pk)
        album.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class PlaylistSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Playlist
        fields = ('user', 'title')


class AlbumSerializer(serializers.ModelSerializer):
    playlists = PlaylistSerializer(many=True)

    class Meta:
        model = Album
        fields = ('id', 'album_title', 'year_created', 'playlists')


class CreateAlbumSerializer (serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'album_title', 'year_created')
