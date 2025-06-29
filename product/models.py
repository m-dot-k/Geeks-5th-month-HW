from django.db import models
from django.db.models import Avg

class Category (models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name
    
    def product_count(self):
        return Product.objects.filter(category = self).count()

class Product (models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title
    
    def average_rating(self):
        return self.reviews.aggregate(Avg('stars'))['stars__avg']

STARS = (
    (i, '*' * i) for i in range (1,6)
)

class Review (models.Model):
    text = models.TextField(max_length=255)
    stars = models.IntegerField(choices = STARS, null = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text
    
    