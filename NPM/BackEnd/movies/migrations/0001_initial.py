# Generated by Django 3.2.13 on 2022-11-22 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('original_title', models.CharField(blank=True, max_length=100, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('poster_path', models.CharField(blank=True, max_length=300, null=True)),
                ('backdrop_path', models.CharField(blank=True, max_length=300, null=True)),
                ('genres', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
    ]
