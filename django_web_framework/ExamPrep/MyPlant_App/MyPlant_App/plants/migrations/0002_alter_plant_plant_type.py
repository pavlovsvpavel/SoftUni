# Generated by Django 5.0.2 on 2024-02-23 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor', 'Indoor Plants')], max_length=14),
        ),
    ]
