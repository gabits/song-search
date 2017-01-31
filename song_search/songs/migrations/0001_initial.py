# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-31 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=512)),
                ('song', models.CharField(max_length=512)),
            ],
        ),
    ]
