# Generated by Django 1.10.7 on 2017-05-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
