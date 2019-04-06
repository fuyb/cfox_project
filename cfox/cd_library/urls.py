#! -*- coding: utf-8 -*-

from django.urls import path
from rest_framework import routers

from .views import AlbumViewSet

router = routers.SimpleRouter()
router.register(r'albums', AlbumViewSet, basename='Album')

urlpatterns = router.urls
