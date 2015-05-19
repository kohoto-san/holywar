# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0030_remove_thread_vote_for_argument'),
    ]

    operations = [
        migrations.AddField(
            model_name='threadcomments',
            name='avatar',
            field=models.CharField(default=0, max_length=50),
            preserve_default=True,
        ),
    ]
