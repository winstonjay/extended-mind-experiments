# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hally_v01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='theKey',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]