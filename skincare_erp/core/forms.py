# core/forms.py
from django import forms
from .models import Product, Order
from .models import Budget, Transaction, CashFlow


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'discount', 'stock']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'customer_name', 'customer_address', 'customer_phone']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'amount', 'start_date', 'end_date']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['description', 'amount', 'date', 'transaction_type', 'budget']

class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['date', 'amount', 'cashflow_type', 'description', 'transaction']
