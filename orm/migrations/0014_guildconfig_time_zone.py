# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0013_guildconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildconfig',
            name='time_zone',
            field=models.CharField(default='America/New_York', max_length=50),
            preserve_default=False,
        ),
    ]
