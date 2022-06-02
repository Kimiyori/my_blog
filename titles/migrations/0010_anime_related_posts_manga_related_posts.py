# Generated by Django 4.0.1 on 2022-05-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_delete_related'),
        ('titles', '0009_alter_anime_description_alter_anime_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='related_posts',
            field=models.ManyToManyField(blank=True, related_name='%(class)s', to='post.Post'),
        ),
        migrations.AddField(
            model_name='manga',
            name='related_posts',
            field=models.ManyToManyField(blank=True, related_name='%(class)s', to='post.Post'),
        ),
    ]