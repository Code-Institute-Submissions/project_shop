# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-27 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_review_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='products',
        ),
    ]
