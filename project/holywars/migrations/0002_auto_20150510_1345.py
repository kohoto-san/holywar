# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holywars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HolywarArgument',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('argument_for', models.CharField(max_length=1)),
                ('argument', models.CharField(max_length=100)),
                ('holywar', models.ForeignKey(to='holywars.Holywar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='holywar',
            name='holywar_name',
        ),
        migrations.AddField(
            model_name='holywar',
            name='holywar_object_1',
            field=models.CharField(max_length=50, default='True'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='holywar',
            name='holywar_object_2',
            field=models.CharField(max_length=50, default='True'),
            preserve_default=True,
        ),
    ]
