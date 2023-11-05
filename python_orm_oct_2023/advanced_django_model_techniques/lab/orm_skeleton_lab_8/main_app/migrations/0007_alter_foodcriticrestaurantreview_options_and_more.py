# Generated by Django 4.2.4 on 2023-11-05 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_foodcriticrestaurantreview_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodcriticrestaurantreview',
            options={'ordering': ['-rating'], 'verbose_name': 'Food Critic Review', 'verbose_name_plural': 'Food Critic Reviews'},
        ),
        migrations.AlterModelOptions(
            name='menureview',
            options={'ordering': ['-rating'], 'verbose_name': 'Menu Review', 'verbose_name_plural': 'Menu Reviews'},
        ),
        migrations.AlterModelOptions(
            name='regularrestaurantreview',
            options={'ordering': ['-rating'], 'verbose_name': 'Restaurant Review', 'verbose_name_plural': 'Restaurant Reviews'},
        ),
    ]
