# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0025_auto_20150517_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='comments',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
