# Generated by Django 4.2.5 on 2023-10-07 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_order_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order_id',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
