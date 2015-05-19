# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0011_threadcomments_i_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threadcomments',
            name='i_like',
        ),
    ]
