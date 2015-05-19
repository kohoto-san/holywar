# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('holywars', '0018_auto_20150515_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='HolywarLike',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('holywar', models.ForeignKey(to='holywars.Holywar')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='holywar',
            name='holywar_likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
