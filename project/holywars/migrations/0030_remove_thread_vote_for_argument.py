# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0029_auto_20150518_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='vote_for_argument',
        ),
    ]
