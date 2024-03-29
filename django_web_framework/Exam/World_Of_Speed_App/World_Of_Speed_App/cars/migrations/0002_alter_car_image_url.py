# Generated by Django 5.0.2 on 2024-02-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image_url',
            field=models.URLField(error_messages={'unique': 'This image URL is already in use! Provide a new one.'}, unique=True, verbose_name='Image URL'),
        ),
    ]
