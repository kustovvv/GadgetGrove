# Generated by Django 4.2.5 on 2023-10-07 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_brand_category_item_delete_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
    ]
