from django.db import models

# Create your models here.

class Playlist(models.Model):
    genre_title = models.CharField(max_length=40)
    def __str__(self):
        return self.title

class Genre(models.Model):
    genre_title = models.CharField(max_length=40)
    def __str__(self):
        return self.title