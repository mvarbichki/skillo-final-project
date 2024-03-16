# Generated by Django 5.0.3 on 2024-03-13 08:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='users_likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]