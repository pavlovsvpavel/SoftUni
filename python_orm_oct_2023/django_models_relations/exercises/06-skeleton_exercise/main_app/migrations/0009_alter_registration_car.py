# Generated by Django 4.2.4 on 2023-11-02 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='car',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.car'),
        ),
    ]