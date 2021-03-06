# Generated by Django 3.0.3 on 2020-08-24 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeid', models.CharField(max_length=10, unique=True)),
                ('map', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('place_name', models.CharField(max_length=100)),
                ('place_img', models.ImageField(null=True, upload_to='')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State')),
            ],
        ),
    ]
