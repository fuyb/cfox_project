#! -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('pk', 'tilte', 'artist', 'date_published', 'genre', 'cover', 
                  'date_modified', 'created')


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('pk', 'tilte', 'artist', 'album', 'date_published', 'genre',
                  'cover', 'filepath', 'file_size', 'lrc', 'date_modified',
                  'created')
