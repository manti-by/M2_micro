# Generated by Django 1.10.7 on 2017-05-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("profiles", "0002_auto_20170419_1251")]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="gallery_ready",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="preview_ready",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="thumbnail_ready",
            field=models.BooleanField(default=False),
        ),
    ]
