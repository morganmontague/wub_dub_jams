from django.contrib import admin
from .models import Song, Genre, Playlist, Artist, Album
# Register your models here.
admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Playlist)
admin.site.register(Artist)
admin.site.register(Album)