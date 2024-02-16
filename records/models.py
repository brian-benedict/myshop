from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     price_bought = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     quantity_available = models.IntegerField()
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
#     minimum_quantity = models.IntegerField(default=0)  # New field for minimum quantity



#     def __str__(self):
#         return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_bought = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity_available = models.IntegerField(default=0)  # Set a default value
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    minimum_quantity = models.IntegerField(default=0)  # New field for minimum quantity

    def __str__(self):
        return self.name








from django.db import models

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    product_reserved = models.ForeignKey(Product, on_delete=models.CASCADE)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.product_reserved}"







# class ReservationPayment(models.Model):
#     reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"Payment of {self.amount} for {self.reservation}"

class ReservationPayment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update reservation status when a payment is added
        self.reservation.paid = True
        self.reservation.save()

    def __str__(self):
        return f"Payment of {self.amount} for {self.reservation}"





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
