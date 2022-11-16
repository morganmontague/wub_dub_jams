from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=300, null=False, default="Untiltled")
    duration = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    plays = models.PositiveIntegerField(null=True)
    explicit = models.BooleanField()
    genre = models.ForeignKey(
        "Genre",
        # related_name="menu_item_by_cuisines",
        on_delete=models.CASCADE,
    null=True)
    playlist = models.ManyToManyField(
        "Playlist",
        )
    album = models.ManyToManyField(
        "Album",
        )
    # artist = models.ManyToManyField(
    #     "Artist",
    #     )
    def __str__(self):
        return self.title


class Playlist(models.Model):
    genre_title = models.CharField(max_length=40, null=False, default="Playlist Wub Dub")
    def __str__(self):
        return self.title

class Genre(models.Model):
    genre_title = models.CharField(max_length=40, null=False, default="Unknown")
    def __str__(self):
        return self.title

class Album(models.Model):
    album_title = models.CharField(max_length=40, null=True, default="Single")
    def __str__(self):
        return self.title

# class Artist(models.Model):
#     album_title = models.CharField(max_length=40, null=False, default="Unknown")
#     def __str__(self):
#         return self.title