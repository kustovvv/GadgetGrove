# Generated by Django 4.2.5 on 2023-11-09 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0028_delete_shoppingcartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]