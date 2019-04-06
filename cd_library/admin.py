#! -*- coding:utf-8 -*-
from django.contrib import admin

from .models import *

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created', 'deleted')
    search_fields = ('name',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('pk', 'artist', 'title', 'created', 'deleted')
    search_fields = ('title', 'artist__name')
    raw_id_fields = ('artist',)


class MusicAdmin(admin.ModelAdmin):
    list_display = ('pk', 'artist', 'title', 'created', 'deleted')
    search_fields = ('title', 'artist__name')
    raw_id_fields = ('artist', 'album')
    exclude = ('filepath',)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Music, MusicAdmin)
