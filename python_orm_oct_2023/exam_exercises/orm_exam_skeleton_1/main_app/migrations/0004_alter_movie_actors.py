# Generated by Django 4.2.4 on 2023-11-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actor_movies', to='main_app.actor'),
        ),
    ]
