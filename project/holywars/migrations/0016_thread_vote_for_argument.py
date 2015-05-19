# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0015_auto_20150514_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='vote_for_argument',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
