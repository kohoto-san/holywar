# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0024_auto_20150517_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holywar',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default='2000-10-10 10:10'),
            preserve_default=True,
        ),
    ]
