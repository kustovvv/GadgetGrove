# Generated by Django 4.2.5 on 2023-11-09 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0030_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
