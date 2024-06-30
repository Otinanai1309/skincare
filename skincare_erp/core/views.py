from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product, Order
from .models import Budget, Transaction, CashFlow
from .models import Supplier, PurchaseOrder, PurchaseOrderItem, InventoryForecast


from .forms import ProductForm, OrderForm
from .forms import BudgetForm, TransactionForm, CashFlowForm
from .forms import SupplierForm, PurchaseOrderForm, PurchaseOrderItemForm, InventoryForecastForm


def home(request):
    return render(request, 'core/home.html')

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'core/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'core/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'core/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

# Order Views
class OrderListView(ListView):
    model = Order
    template_name = 'core/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'core/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'core/order_form.html'
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'core/order_form.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'core/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

# Budget Views
class BudgetListView(ListView):
    model = Budget
    template_name = 'core/budget_list.html'
    context_object_name = 'budgets'

class BudgetDetailView(DetailView):
    model = Budget
    template_name = 'core/budget_detail.html'
    context_object_name = 'budget'

class BudgetCreateView(CreateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'core/budget_form.html'
    success_url = reverse_lazy('budget_list')

class BudgetUpdateView(UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'core/budget_form.html'
    success_url = reverse_lazy('budget_list')

class BudgetDeleteView(DeleteView):
    model = Budget
    template_name = 'core/budget_confirm_delete.html'
    success_url = reverse_lazy('budget_list')

# Transaction Views
class TransactionListView(ListView):
    model = Transaction
    template_name = 'core/transaction_list.html'
    context_object_name = 'transactions'

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'core/transaction_detail.html'
    context_object_name = 'transaction'

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'core/transaction_form.html'
    success_url = reverse_lazy('transaction_list')

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'core/transaction_form.html'
    success_url = reverse_lazy('transaction_list')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'core/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')

# CashFlow Views
class CashFlowListView(ListView):
    model = CashFlow
    template_name = 'core/cashflow_list.html'
    context_object_name = 'cashflows'

class CashFlowDetailView(DetailView):
    model = CashFlow
    template_name = 'core/cashflow_detail.html'
    context_object_name = 'cashflow'

class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'core/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')

class CashFlowUpdateView(UpdateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'core/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')

class CashFlowDeleteView(DeleteView):
    model = CashFlow
    template_name = 'core/cashflow_confirm_delete.html'
    success_url = reverse_lazy('cashflow_list')
    
# Supplier Views
class SupplierListView(ListView):
    model = Supplier
    template_name = 'core/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'core/supplier_detail.html'
    context_object_name = 'supplier'

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'core/supplier_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'core/supplier_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'core/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')

# PurchaseOrder Views
class PurchaseOrderListView(ListView):
    model = PurchaseOrder
    template_name = 'core/purchaseorder_list.html'
    context_object_name = 'purchaseorders'

class PurchaseOrderDetailView(DetailView):
    model = PurchaseOrder
    template_name = 'core/purchaseorder_detail.html'
    context_object_name = 'purchaseorder'

class PurchaseOrderCreateView(CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'core/purchaseorder_form.html'
    success_url = reverse_lazy('purchaseorder_list')

class PurchaseOrderUpdateView(UpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'core/purchaseorder_form.html'
    success_url = reverse_lazy('purchaseorder_list')

class PurchaseOrderDeleteView(DeleteView):
    model = PurchaseOrder
    template_name = 'core/purchaseorder_confirm_delete.html'
    success_url = reverse_lazy('purchaseorder_list')

# InventoryForecast Views
class InventoryForecastListView(ListView):
    model = InventoryForecast
    template_name = 'core/inventoryforecast_list.html'
    context_object_name = 'inventoryforecasts'

class InventoryForecastDetailView(DetailView):
    model = InventoryForecast
    template_name = 'core/inventoryforecast_detail.html'
    context_object_name = 'inventoryforecast'

class InventoryForecastCreateView(CreateView):
    model = InventoryForecast
    form_class = InventoryForecastForm
    template_name = 'core/inventoryforecast_form.html'
    success_url = reverse_lazy('inventoryforecast_list')

class InventoryForecastUpdateView(UpdateView):
    model = InventoryForecast
    form_class = InventoryForecastForm
    template_name = 'core/inventoryforecast_form.html'
    success_url = reverse_lazy('inventoryforecast_list')

class InventoryForecastDeleteView(DeleteView):
    model = InventoryForecast
    template_name = 'core/inventoryforecast_confirm_delete.html'
    success_url = reverse_lazy('inventoryforecast_list')
