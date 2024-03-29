# Generated by Django 4.2.4 on 2023-10-24 13:00

from django.db import migrations


def set_item_rarity(apps, schema_editor):
    item = apps.get_model('main_app', 'Item')
    all_items = item.objects.all()

    for c_item in all_items:
        if c_item.price <= 10:
            c_item.rarity = 'Rare'
        elif 11 <= c_item.price <= 20:
            c_item.rarity = 'Very Rare'
        elif 21 <= c_item.price <= 30:
            c_item.rarity = 'Extremely Rare'
        else:
            c_item.rarity = 'Mega Rare'

    item.objects.bulk_update(all_items, ['rarity'])


def reverse_item_rarity(apps, schema_editor):
    item = apps.get_model('main_app', 'Item')
    all_items = item.objects.all()
    item_rarity_default = item._meta.get_field('rarity').default  # get the default from initial table creation

    for c_item in all_items:
        c_item.rarity = item_rarity_default

    item.objects.bulk_update(all_items, ['rarity'])


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0011_item'),
    ]

    operations = [
        migrations.RunPython(set_item_rarity, reverse_code=reverse_item_rarity)
                  ]
