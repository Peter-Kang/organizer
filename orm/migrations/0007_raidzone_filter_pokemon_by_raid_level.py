# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0006_raidzone_filter_eggs'),
    ]

    operations = [
        migrations.AddField(
            model_name='raidzone',
            name='filter_pokemon_by_raid_level',
            field=models.BooleanField(default=True),
        ),
    ]
