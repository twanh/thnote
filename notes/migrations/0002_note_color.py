# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-18 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='color',
            field=models.CharField(default='grey lighten-2', max_length=60),
        ),
    ]
