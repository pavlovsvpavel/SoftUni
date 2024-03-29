# Generated by Django 5.0.1 on 2024-02-07 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_rename_like_photolike'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='photos.petphoto'),
        ),
        migrations.AlterField(
            model_name='photolike',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='photos.petphoto'),
        ),
    ]
