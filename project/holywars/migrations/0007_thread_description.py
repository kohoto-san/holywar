# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0006_auto_20150511_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='description',
            field=models.CharField(default='True', max_length=200),
            preserve_default=True,
        ),
    ]
