# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-28 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0004_auto_20170528_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='title',
            field=models.CharField(choices=[('computer', 'COMPUTER'), ('draws', 'DRAWS'), ('humans', 'HUMANS')], max_length=30),
        ),
    ]
