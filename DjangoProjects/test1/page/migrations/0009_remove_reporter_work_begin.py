# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 21:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_auto_20161124_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporter',
            name='work_begin',
        ),
    ]
