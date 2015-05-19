# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0002_auto_20150510_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('holywar', models.ForeignKey(to='holywars.Holywar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
