# Generated by Django 3.0.8 on 2020-08-06 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20200803_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='disc_gid',
        ),
    ]
