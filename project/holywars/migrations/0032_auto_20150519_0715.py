# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0031_threadcomments_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holywar',
            name='holywar_description_1',
            field=models.CharField(default='True', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='holywar',
            name='holywar_description_2',
            field=models.CharField(default='True', max_length=100),
            preserve_default=True,
        ),
    ]
