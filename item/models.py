from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class CategoryBrand(models.Model):
    category = models.ForeignKey(Category, related_name='category_brands', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='category_brands', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('category', 'brand')

    def __str__(self):
        return f'{self.category} {self.brand}'
    

class Item(models.Model):
    category_brand = models.ForeignKey(CategoryBrand, related_name='items', on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    availability = models.BooleanField(default=False)
    image_url = models.URLField()

    class Meta:
        ordering = ('model',)

    def __str__(self):
        return self.model
    

class Comments(models.Model):
    item = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    comment = models.TextField()
    advantages = models.CharField(max_length=255, null=True, blank=True)
    disadvantages = models.CharField(max_length=255, null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ('-comment_date', )
    
    def __str__(self):
        return f'{self.first_name} for {self.item.model}'