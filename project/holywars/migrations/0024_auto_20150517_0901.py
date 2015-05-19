# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0023_auto_20150517_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holywar',
            name='time_create',
            field=models.TimeField(default=datetime.time(0, 0), auto_now_add=True),
            preserve_default=True,
        ),
    ]
