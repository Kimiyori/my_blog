# Generated by Django 4.0.1 on 2022-05-25 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_preferences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='preferences',
        ),
    ]