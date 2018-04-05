# Generated by Django 1.10.7 on 2017-04-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170419_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='summary_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='summary_ru',
            field=models.TextField(null=True),
        ),
    ]
