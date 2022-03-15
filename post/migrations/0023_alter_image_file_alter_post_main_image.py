# Generated by Django 4.0.1 on 2022-03-05 12:09

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_post_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to=post.models.path),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(upload_to=post.models.main_path),
        ),
    ]