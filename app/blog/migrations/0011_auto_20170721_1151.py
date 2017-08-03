# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-21 11:51
from __future__ import unicode_literals

from django.db import migrations


def update_translations(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        post.name_by = post.name_ru
        post.meta_by = post.meta_ru
        post.summary_by = post.summary_ru
        post.description_by = post.description_ru
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170717_1218'),
    ]

    operations = [
        migrations.RunPython(update_translations),
    ]
