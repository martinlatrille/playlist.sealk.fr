# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20140914_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='adress',
            field=models.CharField(max_length=256, default=None),
            preserve_default=False,
        ),
    ]
