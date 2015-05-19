# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0021_auto_20150517_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holywar',
            name='holywar_likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='holywar',
            name='threads',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
