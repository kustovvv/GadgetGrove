from django.db import models
from django.contrib.auth.models import User

from item.models import Item

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, related_name='shippingAddresses', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ('user',)
        verbose_name_plural = 'Shipping addresses'

    def __str__(self):
        return f'{self.user.username} {self.orders.first()}'


class ContactInfo(models.Model):
    user = models.ForeignKey(User, related_name='contactInfos', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        ordering = ('user', )

    def __str__(self):
        return f'{self.user.username} {self.orders.first()}'


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    contact_info = models.ForeignKey(ContactInfo, related_name='orders', on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    total_price = models.FloatField(null=True)

    class Meta:
        ordering = ('order_date',)
    
    def __str__(self):
        return f'Order by {self.user.username} at {self.order_date} with status "{self.status}";'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderItems', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='orderItems', on_delete=models.CASCADE)
    amount = models.IntegerField()
    item_price = models.FloatField()

    class Meta:
        ordering = ('order',)
    
    def __str__(self):
        return f'{self.item.model} {self.amount} items in {self.order}'
    

class ShoppingCartItem(models.Model):
    user = models.ForeignKey(User, related_name='cartItems', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='cartItems', on_delete=models.CASCADE)
    amount = models.IntegerField()
