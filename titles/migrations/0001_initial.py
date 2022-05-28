# Generated by Django 4.0.1 on 2022-04-25 20:06

from django.db import migrations, models
import django.db.models.deletion
import titles.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('premiere', models.DateField(blank=True, null=True)),
                ('episodes', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=titles.models.image_path_anime)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='AnimeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(default='', max_length=250)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('pseudonym', models.CharField(blank=True, max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='authors/')),
            ],
        ),
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(default='', max_length=250)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(default='', max_length=250)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('premiere', models.DateField(blank=True)),
                ('volumes', models.IntegerField(blank=True, null=True)),
                ('chapters', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=titles.models.image_path_manga)),
                ('description', models.TextField(blank=True)),
                ('authors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manga', to='titles.authors')),
                ('demographic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manga', to='titles.demographic')),
                ('genre', models.ManyToManyField(blank=True, related_name='manga', to='titles.Genre')),
                ('magazine', models.ManyToManyField(blank=True, related_name='manga', to='titles.Magazine')),
            ],
            options={
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='MangaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(default='', max_length=250)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, upload_to='publishers/')),
                ('slug', models.SlugField(default='', max_length=250)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, upload_to='studios/')),
                ('slug', models.SlugField(default='', max_length=250)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_name', models.CharField(blank=True, max_length=300, null=True)),
                ('russian_name', models.CharField(blank=True, max_length=300, null=True)),
                ('english_name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SequelPrequelManga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prequel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sequel', to='titles.manga')),
                ('sequel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prequel', to='titles.manga')),
            ],
        ),
        migrations.CreateModel(
            name='SequelPrequelAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prequel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sequel', to='titles.anime')),
                ('sequel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prequel', to='titles.anime')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_item', to='titles.anime')),
                ('manga', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_item', to='titles.manga')),
            ],
        ),
        migrations.AddField(
            model_name='manga',
            name='publisher',
            field=models.ManyToManyField(blank=True, related_name='manga', to='titles.Publisher'),
        ),
        migrations.AddField(
            model_name='manga',
            name='theme',
            field=models.ManyToManyField(blank=True, related_name='manga', to='titles.Theme'),
        ),
        migrations.AddField(
            model_name='manga',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manga', to='titles.title'),
        ),
        migrations.AddField(
            model_name='manga',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manga', to='titles.mangatype'),
        ),
        migrations.AddField(
            model_name='authors',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors_artist', to='titles.authortable'),
        ),
        migrations.AddField(
            model_name='authors',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors_author', to='titles.authortable'),
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='anime', to='titles.Genre'),
        ),
        migrations.AddField(
            model_name='anime',
            name='studio',
            field=models.ManyToManyField(blank=True, related_name='anime', to='titles.Studio'),
        ),
        migrations.AddField(
            model_name='anime',
            name='theme',
            field=models.ManyToManyField(blank=True, related_name='anime', to='titles.Theme'),
        ),
        migrations.AddField(
            model_name='anime',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anime', to='titles.title'),
        ),
        migrations.AddField(
            model_name='anime',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anime', to='titles.animetype'),
        ),
        migrations.CreateModel(
            name='Adaptation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adaptation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='based_on', to='titles.anime')),
                ('based_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adaptation', to='titles.manga')),
            ],
        ),
    ]