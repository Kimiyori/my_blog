# Generated by Django 4.0.1 on 2022-01-10 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0017_alter_anime_genres_alter_anime_studio'),
    ]

    operations = [
        migrations.AddField(
            model_name='demographic',
            name='slug',
            field=models.SlugField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='type',
            name='slug',
            field=models.SlugField(default='', max_length=250),
        ),
    ]
