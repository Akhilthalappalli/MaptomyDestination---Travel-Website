# Generated by Django 3.0.3 on 2020-08-26 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='placeid',
        ),
    ]
