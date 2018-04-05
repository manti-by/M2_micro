# Generated by Django 1.10.7 on 2017-05-04 08:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created, UTC')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('meta', models.TextField(blank=True, null=True)),
                ('is_sent', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
