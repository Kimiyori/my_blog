# Generated by Django 4.0.1 on 2022-04-15 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0020_alter_manga_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manga',
            old_name='genres',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='manga',
            old_name='themes',
            new_name='theme',
        ),
    ]