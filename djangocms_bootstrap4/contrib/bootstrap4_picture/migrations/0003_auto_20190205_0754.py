# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-05 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_picture', '0002_auto_20190128_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bootstrap4picture',
            name='use_responsive_image',
        ),
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='use_automatic_scaling',
            field=models.BooleanField(default=True, help_text='Uses the placeholder dimenstions to automatically calculate the size.', verbose_name='Automatic scaling'),
        ),
    ]
