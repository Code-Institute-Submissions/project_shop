# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-21 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20200218_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(max_length=100),
        ),
    ]
