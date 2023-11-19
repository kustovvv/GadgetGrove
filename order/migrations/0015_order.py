# Generated by Django 4.2.5 on 2023-10-31 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0014_remove_orderitem_item_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField(null=True)),
                ('contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.contactinfo')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.paymentmethod')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.shippingaddress')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.orderstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-order_date',),
            },
        ),
    ]