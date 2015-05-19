# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('holywars', '0016_thread_vote_for_argument'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadLike',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('thread', models.ForeignKey(to='holywars.Thread')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='thread',
            name='i_like',
            field=models.CharField(max_length=1, default=0),
            preserve_default=True,
        ),
    ]
