# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-08 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_carousel', '0002_bootstrap4carousel_carousel_aspect_ratio'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4carouselslide',
            name='link',
            field=models.CharField(blank=True, max_length=2040, verbose_name='Link'),
        ),
    ]
