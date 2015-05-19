# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0013_threadcomments_i_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='holywar',
            name='holywar_description_1',
            field=models.CharField(max_length=200, default='True'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='holywar',
            name='holywar_description_2',
            field=models.CharField(max_length=200, default='True'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='holywar',
            name='time_create',
            field=models.DateTimeField(default='2000-10-10 10:10', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='holywar',
            name='holywar_object_1',
            field=models.CharField(max_length=20, default='True'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='holywar',
            name='holywar_object_2',
            field=models.CharField(max_length=20, default='True'),
            preserve_default=True,
        ),
    ]
