# Generated by Django 4.2.5 on 2023-11-08 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_orderitem'),
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
