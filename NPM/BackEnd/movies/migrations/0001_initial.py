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
                ('genre_name', models.CharField(max_length=20)),
                ('genre_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_path', models.CharField(max_length=100, null=True)),
                ('backdrop_path', models.CharField(max_length=100, null=True)),
                ('original_title', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('original_language', models.CharField(max_length=20)),
                ('runtime', models.IntegerField()),
                ('revenue', models.IntegerField()),
                ('budget', models.IntegerField()),
                ('vote_count', models.IntegerField()),
                ('adult', models.IntegerField()),
                ('movie_id', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('popularity', models.FloatField()),
                ('release_date', models.DateField()),
                ('overview', models.TextField(blank=True)),
                ('genre', models.ManyToManyField(related_name='same_genre_movies', to='movies.Genre')),
            ],
        ),
    ]
