# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-18 12:19
from __future__ import unicode_literals

import core.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created, UTC')),
                ('original', models.ImageField(blank=True, null=True, upload_to=core.utils.original_name, verbose_name='Image')),
                ('thumb', models.ImageField(blank=True, null=True, upload_to=core.utils.thumb_name, verbose_name='Thumbnail')),
                ('preview', models.ImageField(blank=True, null=True, upload_to=core.utils.preview_name, verbose_name='Preview Image')),
                ('gallery', models.ImageField(blank=True, null=True, upload_to=core.utils.gallery_name, verbose_name='Gallery Image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]