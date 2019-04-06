# Generated by Django 2.2 on 2019-04-06 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_modified', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='删除？')),
                ('sort_index', models.IntegerField(default=0, verbose_name='排序索引')),
                ('title', models.CharField(default='album', max_length=1024, verbose_name='标题')),
                ('date_published', models.DateField(verbose_name='发布时间')),
                ('genre', models.CharField(choices=[('R', 'Rock'), ('B', 'Blues'), ('J', 'Jazz'), ('P', 'Pop'), ('MX', 'Mixture')], default='P', max_length=1, verbose_name='风格')),
                ('cover', models.URLField(blank=True, default=None, max_length=2048, null=True, verbose_name='封面链接')),
            ],
            options={
                'verbose_name': '专集',
                'verbose_name_plural': '专集',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_modified', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='删除？')),
                ('sort_index', models.IntegerField(default=0, verbose_name='排序索引')),
                ('name', models.CharField(default='name', max_length=128, verbose_name='名字')),
                ('birthday', models.DateField(default=None, verbose_name='生日')),
                ('description', models.TextField(blank=True, null=True, verbose_name='介绍')),
                ('date_death', models.DateField(blank=True, default=None, null=True, verbose_name='去世日期')),
            ],
            options={
                'verbose_name': '艺术家',
                'verbose_name_plural': '艺术家',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('date_modified', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='删除？')),
                ('sort_index', models.IntegerField(default=0, verbose_name='排序索引')),
                ('title', models.CharField(default='music', max_length=1024, verbose_name='标题')),
                ('date_published', models.DateField(verbose_name='发布时间')),
                ('genre', models.CharField(choices=[('R', 'Rock'), ('B', 'Blues'), ('J', 'Jazz'), ('P', 'Pop'), ('MX', 'Mixture')], default='P', max_length=1, verbose_name='风格')),
                ('cover', models.URLField(blank=True, default=None, max_length=2048, null=True, verbose_name='封面链接')),
                ('filepath', models.FilePathField(default='/404', max_length=2048, verbose_name='文件地址')),
                ('file_size', models.PositiveIntegerField(default=0, verbose_name='文件大小')),
                ('lrc', models.TextField(blank=True, null=True, verbose_name='歌词')),
                ('album', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='cd_library.Album', verbose_name='专集')),
                ('artist', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='cd_library.Artist', verbose_name='艺术家')),
            ],
            options={
                'verbose_name': '音乐',
                'verbose_name_plural': '音乐',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='cd_library.Artist', verbose_name='艺术家'),
        ),
    ]
