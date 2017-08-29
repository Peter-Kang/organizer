# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 02:37
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import orm.models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_botonlychannel'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaidZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=64)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('radius', models.DecimalField(decimal_places=1, default=5.0, max_digits=3)),
                ('active', models.BooleanField(default=True)),
                ('filters', django.contrib.postgres.fields.jsonb.JSONField(default=orm.models.filter_default)),
            ],
        ),
    ]
