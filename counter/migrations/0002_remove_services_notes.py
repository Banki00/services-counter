# Generated by Django 3.1.7 on 2021-03-31 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='notes',
        ),
    ]
