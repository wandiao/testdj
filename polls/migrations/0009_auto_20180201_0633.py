# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20180201_0339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='destory_time',
            new_name='destroy_time',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='is_destoryed',
            new_name='is_destroyed',
        ),
    ]
