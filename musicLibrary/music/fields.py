from rest_framework import serializers
from .models import *



class albumfield(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.album_title

    def to_internal_value(self, data):
        return Album.objects.get(album_title=data)



class artistfield(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.artist_title

    def to_internal_value(self, data):
        return Artist.objects.get(artist_title=data)



class playlistfield(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.playlist_title

    def to_internal_value(self, data):
        return Playlist.objects.get(playlist_title=data)



# def to_internal_value(self, data):
#         obj, created = Album.objects.get_or_create(**data)
#         return obj

# class genrefield(serializers.RelatedField):
#     def to_representation(self, instance):
#         return instance.genre_title

# def to_internal_value(self, data):
#         obj, created = Album.objects.get_or_create(**data)
#         return obj