#! -*- coding: utf-8 -*-

from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin

from .models import *

class ArtistSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('pk', 'name', 'birthday', 'date_death', 'description')


class AlbumSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('pk', 'title', 'artist', 'date_published', 'genre', 'cover', 
                  'date_modified', 'created')


class MusicSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('pk', 'title', 'artist', 'album', 'date_published', 'genre',
                  'cover', 'filepath', 'file_size', 'lrc', 'date_modified',
                  'created')
