# Generated by Django 4.2.4 on 2023-11-03 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_veterinarian_zookeeper'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZooDisplayAnimal',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.animal',),
        ),
    ]
