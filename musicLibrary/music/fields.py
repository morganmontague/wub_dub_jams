from rest_framework import serializers
from .models import *

class albumfield(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.title

    def to_internal_value(self, data):
        return Album.objects.get(name=data)

class artistfield(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.title

    def to_internal_value(self, data):
        return Artist.objects.get(name=data)

class playlistfield(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.title

    def to_internal_value(self, data):
        return Playlist.objects.get(name=data)

# class genrefield(serializers.RelatedField):
#     def to_representation(self, instance):
#         return instance.genre_title

#     def to_internal_value(self, data):
#         return Genre.objects.get(name=data)