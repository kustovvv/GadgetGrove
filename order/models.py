from django.db import models

from item.models import Item
from authentication.models import User as CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

class ShippingAddress(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ('city',)
        verbose_name_plural = 'Shipping addresses'


class OrderStatus(models.Model):
    status = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Order Statuses'

    def __str__(self):
        return self.status
    

class PaymentMethod(models.Model):
    method = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.method
    

class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        ordering = ('phone_number', )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name='orders', on_delete=models.CASCADE)
    seller = models.ForeignKey(CustomUser, related_name='order_seller', on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, related_name='orders', on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, related_name='orders', on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, related_name='orders', on_delete=models.CASCADE)
    contact_info = models.ForeignKey(ContactInfo, related_name='orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(null=True)
    comment = models.TextField()

    class Meta:
        ordering = ('-order_date',)
    
    def __str__(self):
        return f'Order by {self.user.username} at {self.order_date} with status "{self.status}";'


class OrderReview(models.Model):
    order = models.ForeignKey(Order, related_name='order_reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return f'From {self.order.user.username} to {self.order.seller.username}'


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
    user = models.ForeignKey(CustomUser, related_name='cartItems', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='cartItems', on_delete=models.CASCADE)
    amount = models.IntegerField()