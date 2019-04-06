from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

# Create your models here.
class Artist(BaseModel):
    name = models.CharField(_(u'名字'), default='name', max_length=128)
    birthday = models.DateField(_(u'生日'), default=None) 
    description = models.TextField(_(u'介绍'), null=True, blank=True)
    date_death = models.DateField(_(u'去世日期'), null=True, blank=True, default=None) 

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'艺术家')
        verbose_name_plural = _(u'艺术家')


GENRE_CHOICES = (
    ('R', 'Rock'),
    ('B', 'Blues'),
    ('J', 'Jazz'),
    ('P', 'Pop'),
    ('MX', 'Mixture'),
)


class Album(BaseModel):
    artist = models.ForeignKey('Artist', default=None, null=True, 
                               on_delete=models.SET_DEFAULT, verbose_name=_(u'艺术家'))
    title = models.CharField(_(u'标题'), default='album', max_length=1024)
    date_published = models.DateField(_(u'发布时间'))
    genre = models.CharField(_(u'风格'), max_length=1, default='P', choices=GENRE_CHOICES)
    cover = models.URLField(_(u'封面链接'), max_length=2048, default=None, null=True, blank=True)

    def __unicode__(self):
        return "{title} by {artist}, {year}".format(
                title=self.title, 
                artist=self.artist,
                year=self.date_published.year)

    class Meta:
        verbose_name = _(u'专集')
        verbose_name_plural = _(u'专集')


class Music(BaseModel):
    album = models.ForeignKey('Album', default=None, null=True, 
                              on_delete=models.SET_DEFAULT, verbose_name=_(u'专集'))
    artist = models.ForeignKey('Artist', default=None, null=True, 
                              on_delete=models.SET_DEFAULT, verbose_name=_(u'艺术家'))
    title = models.CharField(_(u'标题'), default='music', max_length=1024)
    date_published = models.DateField(_(u'发布时间'))
    genre = models.CharField(_(u'风格'), max_length=1, default='P', choices=GENRE_CHOICES)
    cover = models.URLField(_(u'封面链接'), max_length=2048, default=None, null=True, blank=True)
    filepath = models.FilePathField(_(u'文件地址'), max_length=2048, default='/404')
    file_size = models.PositiveIntegerField(_(u'文件大小'), default=0)
    lrc = models.TextField(_(u'歌词'), null=True, blank=True)

    def __unicode__(self):
        return "{title} by {artist} -- {album}".format(
                title=self.title,
                artist=self.artist,
                album=self.album)

    class Meta:
        verbose_name = _(u'音乐')
        verbose_name_plural = _(u'音乐')
