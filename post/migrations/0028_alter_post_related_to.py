# Generated by Django 4.0.1 on 2022-03-15 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0027_rename_url_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='related_to',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='post.related'),
        ),
    ]