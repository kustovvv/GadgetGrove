# Generated by Django 4.2.5 on 2023-11-09 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0023_shoppingcartitem_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcartitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='shoppingcartitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='ShoppingCartItem',
        ),
    ]
