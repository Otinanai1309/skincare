from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product, Order
from .models import Budget, Transaction, CashFlow

from .forms import ProductForm, OrderForm
from .forms import BudgetForm, TransactionForm, CashFlowForm

def home(request):
    return render(request, 'core/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'core/product_detail.html', {'product': product})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'core/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'core/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'core/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'core/order_form.html', {'form': form})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'core/order_detail.html', {'order': order})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'core/order_form.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'core/order_confirm_delete.html', {'order': order})
  

def home(request):
    return render(request, 'core/home.html')

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