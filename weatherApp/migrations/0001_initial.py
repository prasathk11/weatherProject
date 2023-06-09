# Generated by Django 3.2.18 on 2023-04-19 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityWeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, unique=True)),
                ('country_code', models.CharField(max_length=2)),
                ('coordinate', models.CharField(max_length=100)),
                ('temp', models.FloatField(default=0.0)),
                ('pressure', models.IntegerField(default=0.0)),
                ('humidity', models.IntegerField(default=0.0)),
                ('main', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=10)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
