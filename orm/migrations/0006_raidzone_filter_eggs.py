# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0005_raid_hatch_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='raidzone',
            name='filter_eggs',
            field=models.BooleanField(default=True),
        ),
    ]
