# Generated by Django 3.0.3 on 2020-09-01 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200901_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top_list',
            name='t_description',
            field=models.CharField(max_length=1500),
        ),
    ]
