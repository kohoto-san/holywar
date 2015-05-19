# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0003_thread'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadComments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('thread', models.ForeignKey(to='holywars.Thread')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='thread',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
