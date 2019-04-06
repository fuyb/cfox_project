#! -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CdLibraryConfig(AppConfig):
    name = 'cd_library'
    verbose_name = _(u'CD曲库')
