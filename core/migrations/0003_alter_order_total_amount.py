# Generated by Django 4.2.5 on 2023-10-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_order_options_alter_orderitem_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.FloatField(blank=True),
        ),
    ]