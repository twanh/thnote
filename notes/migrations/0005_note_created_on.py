# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-19 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_note_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
