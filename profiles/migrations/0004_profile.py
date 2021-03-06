# Generated by Django 3.0.8 on 2020-07-29 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='images/')),
                ('bio', models.TextField(blank=True)),
                ('twitch', models.CharField(blank=True, max_length=100)),
                ('guild_id', models.CharField(max_length=200)),
                ('disc_uid', models.CharField(max_length=200)),
                ('exp', models.IntegerField()),
                ('lvl', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
