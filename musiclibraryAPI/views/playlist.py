"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from musiclibraryAPI.models import Playlist
from django.contrib.auth.models import User

from musiclibraryAPI.views.album import AlbumSerializer


class PlaylistView(ViewSet):
    """Music Library Album view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single album

        Returns:
            Response -- JSON serialized album
        """

        playlist = Playlist.objects.get(pk=pk)

        serializer = PlaylistSerializer(playlist)

        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all playlists

        Returns:
            Response -- JSON serialized list of playlists
        """
        # list of all playlist objects
        # reference playlist model
        # store returned data in a variable

        playlists = Playlist.objects.all()

        # create an instance of a serializer
        serializer = PlaylistSerializer(playlists, many=True)
        # return a response

        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(pk=request.auth.user.id)
        serializer = CreatePlaylistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        playlist = Playlist.objects.get(pk=serializer.data['id'])
        playlist.albums.add(*request.data['albums'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        user = User.objects.get(pk=request.auth.user.id)
        playlist = Playlist.objects.get(pk=pk)

        serializer = CreatePlaylistSerializer(playlist, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        playlist = Playlist.objects.get(pk=pk)
        playlist.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class PlaylistSerializer(serializers.ModelSerializer):

    albums = AlbumSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Playlist
        fields = ('title', 'user', 'albums')


class CreatePlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = ('id', 'title', 'user')
