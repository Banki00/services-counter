# Generated by Django 3.1.7 on 2021-03-27 17:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('counter', '0012_auto_20210327_1657'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddService',
            new_name='Services',
        ),
    ]
