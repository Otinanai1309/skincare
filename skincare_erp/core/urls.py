from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('products/', views.product_list, name='product_list'),
    path('products/new/', views.product_create, name='product_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/new/', views.order_create, name='order_create'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/<int:pk>/edit/', views.order_update, name='order_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
    # Budget URLs
    path('budgets/', views.BudgetListView.as_view(), name='budget_list'),
    path('budgets/new/', views.BudgetCreateView.as_view(), name='budget_create'),
    path('budgets/<int:pk>/', views.BudgetDetailView.as_view(), name='budget_detail'),
    path('budgets/<int:pk>/edit/', views.BudgetUpdateView.as_view(), name='budget_update'),
    path('budgets/<int:pk>/delete/', views.BudgetDeleteView.as_view(), name='budget_delete'),
    # Transaction URLs
    path('transactions/', views.TransactionListView.as_view(), name='transaction_list'),
    path('transactions/new/', views.TransactionCreateView.as_view(), name='transaction_create'),
    path('transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction_detail'),
    path('transactions/<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='transaction_update'),
    path('transactions/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction_delete'),
    # CashFlow URLs
    path('cashflows/', views.CashFlowListView.as_view(), name='cashflow_list'),
    path('cashflows/new/', views.CashFlowCreateView.as_view(), name='cashflow_create'),
    path('cashflows/<int:pk>/', views.CashFlowDetailView.as_view(), name='cashflow_detail'),
    path('cashflows/<int:pk>/edit/', views.CashFlowUpdateView.as_view(), name='cashflow_update'),
    path('cashflows/<int:pk>/delete/', views.CashFlowDeleteView.as_view(), name='cashflow_delete'),
]
