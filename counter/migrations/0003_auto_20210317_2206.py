# Generated by Django 3.1.7 on 2021-03-17 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_auto_20210317_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='haircut',
            old_name='persent_from_price',
            new_name='percent_from_price',
        ),
        migrations.AlterField(
            model_name='typeofwork',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]
