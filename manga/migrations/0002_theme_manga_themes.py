# Generated by Django 4.0.1 on 2022-02-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(default='', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='manga',
            name='themes',
            field=models.ManyToManyField(blank=True, related_name='manga', to='manga.Theme'),
        ),
    ]