# Generated by Django 4.0.1 on 2022-02-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0012_manga_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='description',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]