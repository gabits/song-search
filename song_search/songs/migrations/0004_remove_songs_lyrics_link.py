# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-02 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20170201_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='lyrics_link',
        ),
    ]
