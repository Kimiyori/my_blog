# Generated by Django 4.0.1 on 2022-02-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0007_alter_manga_type_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='english_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='original_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='russiam_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]