# Generated by Django 1.11.15 on 2018-09-11 08:29
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("shortener", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="link",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        )
    ]
