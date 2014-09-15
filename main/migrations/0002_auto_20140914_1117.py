# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('artist', models.CharField(max_length=256)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Playlist',
            new_name='TypePlaylist',
        ),
        migrations.AddField(
            model_name='song',
            name='type',
            field=models.ForeignKey(to='main.TypePlaylist'),
            preserve_default=True,
        ),
    ]
