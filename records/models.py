from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_bought = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity_available = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')

    def __str__(self):
        return self.name





from django.db import models
from .models import Product

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.product} on {self.sale_date}"

    def save(self, *args, **kwargs):
        # Deduct sold quantity from available quantity of the product
        self.product.quantity_available -= self.quantity_sold
        self.product.save()  # Save the updated quantity_available field of the product
        super().save(*args, **kwargs)  # Call the original save() method to save the Sale object





from django.db import models

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateTimeField(auto_now_add=True)  # Automatically set to current date and time

    def __str__(self):
        return self.description
