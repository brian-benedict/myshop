from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')

    def __str__(self):
        return self.name
