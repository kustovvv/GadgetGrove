# Generated by Django 4.2.5 on 2023-10-25 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_remove_shoppingcartitem_item_and_more'),
        ('item', '0015_alter_comments_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='item',
        ),
        migrations.RemoveField(
            model_name='item',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
