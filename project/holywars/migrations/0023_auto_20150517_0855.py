# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0022_auto_20150517_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holywar',
            name='time_create',
            field=models.TimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
