# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0004_auto_20150511_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='time_create',
            field=models.DateTimeField(default='2000-10-10 10:20', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='threadcomments',
            name='time_create',
            field=models.DateTimeField(default='2000-10-10 10:20', auto_now_add=True),
            preserve_default=True,
        ),
    ]
