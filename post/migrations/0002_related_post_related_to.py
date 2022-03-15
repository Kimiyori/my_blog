# Generated by Django 4.0.1 on 2022-03-01 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0020_alter_manga_image'),
        ('anime', '0006_alter_anime_options'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
                ('manga', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manga.manga')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='related_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.related'),
            preserve_default=False,
        ),
    ]