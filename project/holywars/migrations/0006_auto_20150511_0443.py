# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0005_auto_20150511_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='threadcomments',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
