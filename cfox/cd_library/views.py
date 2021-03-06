#! -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

# Create your views here.
class ArtistViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = ArtistSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filteset_fields = ('title', 'name')
    search_fields = ('title', 'name')

    def get_queryset(self):
        return Artist.objects.filter()


class AlbumViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = AlbumSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filteset_fields = ('title', 'artist__name')
    search_fields = ('title', 'artist__name')

    def get_queryset(self):
        return Album.objects.filter()


album_list = AlbumViewSet.as_view({'get': 'list'})
album_detail = AlbumViewSet.as_view({'get': 'retrieve'})


class MusicViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = MusicSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filteset_fields = ('title', 'artist__name')
    search_fields = ('title', 'artist__name')

    def get_queryset(self):
        return Music.objects.filter()


music_list = MusicViewSet.as_view({'get': 'list'})
music_detail = MusicViewSet.as_view({'get': 'retrieve'})
