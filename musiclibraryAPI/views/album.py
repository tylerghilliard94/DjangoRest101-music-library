"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from musiclibraryAPI.models import Album


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
        # list of all album objects
        # reference album model
        # store returned data in a variable

        albums = Album.objects.all()

        # create an instance of a serializer
        serializer = AlbumSerializer(albums, many=True)
        # return a response

        return Response(serializer.data)


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('album_title',)
