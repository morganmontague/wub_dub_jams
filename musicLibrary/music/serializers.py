# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Song, Album, Playlist, Genre, Artist


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ["genre_title"]
    # def create(self, validated_data):
    #     print(validated_data)
    #     obj_genre, created = Genre.objects.get_or_create(genre_title = [validated_data])
    #     genre = obj_genre
    #     genre = Genre.objects.create(**validated_data, genre=obj_genre )
    #     return genre


class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Album
        fields = "__all__"

class ArtistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = "__all__"

class PlaylistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Playlist
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    # album = AlbumSerializer()
    # artist = ArtistSerializer()
    # playlist = PlaylistSerializer()
    class Meta:
        model = Song
        fields = "__all__"
    # def create(self, validated_data):
    #     album = validated_data.pop('album')
    #     obj_album, created = Album.objects.get_or_create(album_title = album['album_title'])
    #     print(obj_album)


    #     artist = validated_data.pop('artist')
    #     obj_artist, created = Artist.objects.get_or_create(artist_title = artist['artist_title'])


    #     playlist = validated_data.pop('playlist')
    #     obj_playlist, created = Playlist.objects.get_or_create(playlist_title = playlist['playlist_title'])
        

    #     genre = validated_data.pop('genre')
    #     obj_genre, created = Genre.objects.get_or_create(genre_title = genre['genre_title'])
    #     song = Song.objects.create(**validated_data, genre=obj_genre, album=objalbum, artist=obj_artist, playlist=obj_playlist)
        # return song
