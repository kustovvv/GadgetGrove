from django.db import models
from django.contrib.auth.models import User

from item.models import Item

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    total_price = models.FloatField(null=True)

    class Meta:
        ordering = ('order_date',)
    
    def __str__(self):
        return f'Order by {self.user_id.username} at {self.order_date} with status "{self.status}";'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderItems', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='orderItems', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_price = models.FloatField()

    class Meta:
        ordering = ('item_price',)
    
    def __str__(self):
        return f'{self.item_id.model} {self.quantity} items in {self.order_id}'
    
class ShoppingCartItem(models.Model):
    user = models.ForeignKey(User, related_name='cartItems', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='cartItems', on_delete=models.CASCADE)
    amount = models.IntegerField()
    