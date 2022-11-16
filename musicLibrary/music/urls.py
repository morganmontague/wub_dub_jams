from django.urls import path, include
from .views import SongViewSet, AlbumViewSet, PlaylistViewSet, ArtistViewSet, GenreViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'songs', SongViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'playlists', PlaylistViewSet)


urlpatterns = [
# path('genre/', GenreAPIView.as_view()),
# path('genre/<str:pk>', GenreAPIView.as_view()),
path('', include(router.urls))
]