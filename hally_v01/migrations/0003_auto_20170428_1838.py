# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hally_v01', '0002_subject_thekey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='noun',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
