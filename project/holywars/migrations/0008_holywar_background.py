# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0007_thread_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='holywar',
            name='background',
            field=models.CharField(max_length=8, default='#99CCFF'),
            preserve_default=True,
        ),
    ]
