# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0012_remove_threadcomments_i_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='threadcomments',
            name='i_like',
            field=models.CharField(max_length=1, default=0),
            preserve_default=True,
        ),
    ]
