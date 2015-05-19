# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0014_auto_20150512_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holywarargument',
            name='argument_for',
            field=models.CharField(max_length=1, default='0'),
            preserve_default=True,
        ),
    ]
