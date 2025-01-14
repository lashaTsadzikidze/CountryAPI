# Generated by Django 5.0.1 on 2024-11-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('capital_city', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('area', models.FloatField()),
                ('official_languages', models.CharField(max_length=300)),
                ('continent', models.CharField(max_length=100)),
                ('main_cities', models.TextField()),
                ('climate', models.FloatField()),
                ('currency', models.CharField(max_length=20)),
                ('gdp', models.FloatField()),
            ],
        ),
    ]
