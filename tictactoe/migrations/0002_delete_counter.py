# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-26 16:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Counter',
        ),
    ]
