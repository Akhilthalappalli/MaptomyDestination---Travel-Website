# Generated by Django 3.0.3 on 2020-09-01 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200901_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top_list',
            name='t_link',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='top_list',
            name='t_map',
            field=models.CharField(max_length=1000),
        ),
    ]
