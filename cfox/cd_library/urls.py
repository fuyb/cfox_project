#! -*- coding: utf-8 -*-

from django.urls import path
from rest_framework import routers

from .views import (
    AlbumViewSet,
    MusicViewSet
)

router = routers.SimpleRouter()
router.register(r'albums', AlbumViewSet, basename='Album')
router.register(r'musics', MusicViewSet, basename='Music')

urlpatterns = router.urls
