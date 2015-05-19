# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0017_auto_20150515_0818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='i_like',
            new_name='thread_i_like',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='likes',
            new_name='thread_likes',
        ),
        migrations.RenameField(
            model_name='threadcomments',
            old_name='i_like',
            new_name='comment_i_like',
        ),
        migrations.AddField(
            model_name='threadcomments',
            name='comment_likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
