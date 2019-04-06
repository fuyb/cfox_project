#! -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

# Create your models here.

class BaseManager(models.Manager):
    def get_queryset(self):
        return supert().get_queryset().filter(deleted=False)

class BaseModel(models.Model):
    created = models.DateTimeField(_(u'创建时间'), auto_now_add=True)
    date_modified = models.DateTimeField(_(u'修改时间'), auto_now_add=True)
    deleted = models.BooleanField(_(u'删除？'), default=False)
    sort_index = models.IntegerField(_(u'排序索引'), default=0)

    objects = BaseManager()

    class Meta:
        abstract = True
        ordering = ('-created', 'sort_index')
