# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0028_remove_holywar_background'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='thread_i_like',
        ),
        migrations.RemoveField(
            model_name='threadcomments',
            name='comment_i_like',
        ),
    ]
