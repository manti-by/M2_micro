# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-19 12:51
from __future__ import unicode_literals

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='gallery',
            new_name='gallery_image',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='original',
            new_name='original_image',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='preview',
            new_name='preview_image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='thumb',
        ),
        migrations.AddField(
            model_name='profile',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to=core.utils.thumb_name, verbose_name='Thumbnail Image'),
        ),
    ]
