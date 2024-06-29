from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView,
    BudgetListView, BudgetDetailView, BudgetCreateView, BudgetUpdateView, BudgetDeleteView,
    TransactionListView, TransactionDetailView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView,
    CashFlowListView, CashFlowDetailView, CashFlowCreateView, CashFlowUpdateView, CashFlowDeleteView,
    home
)

urlpatterns = [
    path('', home, name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/new/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),

    path('budgets/', BudgetListView.as_view(), name='budget_list'),
    path('budgets/new/', BudgetCreateView.as_view(), name='budget_create'),
    path('budgets/<int:pk>/', BudgetDetailView.as_view(), name='budget_detail'),
    path('budgets/<int:pk>/edit/', BudgetUpdateView.as_view(), name='budget_update'),
    path('budgets/<int:pk>/delete/', BudgetDeleteView.as_view(), name='budget_delete'),

    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/new/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('transactions/<int:pk>/edit/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transactions/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),

    path('cashflows/', CashFlowListView.as_view(), name='cashflow_list'),
    path('cashflows/new/', CashFlowCreateView.as_view(), name='cashflow_create'),
    path('cashflows/<int:pk>/', CashFlowDetailView.as_view(), name='cashflow_detail'),
    path('cashflows/<int:pk>/edit/', CashFlowUpdateView.as_view(), name='cashflow_update'),
    path('cashflows/<int:pk>/delete/', CashFlowDeleteView.as_view(), name='cashflow_delete'),
]
