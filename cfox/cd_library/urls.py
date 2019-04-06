#! -*- coding: utf-8 -*-

from django.urls import path
from rest_framework import routers

from .views import (
    AlbumViewSet,
    MusicViewSet,
    ArtistViewSet
)

router = routers.SimpleRouter()
router.register(r'albums', AlbumViewSet, basename='Album')
router.register(r'musics', MusicViewSet, basename='Music')
router.register(r'artists', ArtistViewSet, basename='Artist')

urlpatterns = router.urls
