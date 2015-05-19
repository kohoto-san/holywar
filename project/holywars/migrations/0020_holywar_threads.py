# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0019_auto_20150517_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='holywar',
            name='threads',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
