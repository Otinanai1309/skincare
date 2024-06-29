# core/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)  # New field for stock keeping
    
    def __str__(self):
        return self.name
      
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    customer_address = models.TextField()
    customer_phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Order {self.id} for {self.customer_name}"
      
class Budget(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.description

class CashFlow(models.Model):
    CASHFLOW_TYPES = (
        ('inflow', 'Inflow'),
        ('outflow', 'Outflow'),
    )
    
    date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    cashflow_type = models.CharField(max_length=7, choices=CASHFLOW_TYPES)
    description = models.CharField(max_length=255)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.description} - {self.cashflow_type} - {self.amount}"
