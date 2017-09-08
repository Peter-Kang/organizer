# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0003_raidzone'),
    ]

    operations = [
        migrations.AddField(
            model_name='raid',
            name='is_egg',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='raid',
            name='pokemon_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='raid',
            name='pokemon_number',
            field=models.IntegerField(null=True),
        ),
    ]