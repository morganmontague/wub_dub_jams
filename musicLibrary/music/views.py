from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import GenreSerializer, SongSerializer, ArtistSerializer, AlbumSerializer, PlaylistSerializer
from .models import Song, Album, Playlist, Genre, Artist
from django.forms.models import model_to_dict
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    http_method_names=['get', 'post', 'put', 'delete']

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names=['get', 'post', 'put', 'delete']

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    http_method_names=['get', 'post', 'put', 'delete']

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names=['get', 'post', 'put', 'delete']

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    http_method_names=['get', 'post', 'put', 'delete']





class GenreAPIView(APIView):
    def get_object(Self, pk):
        try:
            return Genre.objects.get(pk = pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = GenreSerializer(data)

        else:
            data = Genre.objects.all()
            serializer = GenreSerializer(data, many=True)

        return Response(serializer.data)

    # Create
    def post(self, request, format=None):
        data =request.data
        serializer = GenreSerializer(data=data)

        # Check if True
        serializer.is_valid(raise_exception=True)

        # Save the data
        serializer.save()

        response = Response()

        response.data = {
            "message": 'Success, Posted a Genre',
            "data": serializer.data,
        }

        return response

    def put(self, request, pk=None, format=None):
        genre_Update = Genre.objects.get(pk=pk)
        data = request.data
        serializer = GenreSerializer(instance=genre_Update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message': "Genre Updated",
            'data': serializer.data
        }
        return response
    
    # def patch():
    #     pass
    # def delete():
        pass

        

