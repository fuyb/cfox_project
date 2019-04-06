#! -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

# Create your views here.

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
