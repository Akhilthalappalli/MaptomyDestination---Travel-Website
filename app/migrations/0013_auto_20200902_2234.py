# Generated by Django 3.0.3 on 2020-09-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200901_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='map',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_link',
            field=models.CharField(max_length=1000),
        ),
    ]
